import random


N, E, S, W = 1, 2, 4, 8


def create_grid(width: int, height: int) -> list[list] | None:

    grid = [[0xF] * width for _ in range(height)]
    forbidden = set()

    if width < 9 or height < 7:
        return grid, forbidden
    else:
        x_center, y_center = width // 2, height // 2

        forbidden.add((x_center - 1, y_center))
        forbidden.add((x_center - 2, y_center))
        forbidden.add((x_center - 3, y_center))
        forbidden.add((x_center - 1, y_center - 2))
        forbidden.add((x_center - 3, y_center - 1))
        forbidden.add((x_center - 3, y_center - 2))
        forbidden.add((x_center - 1, y_center - 1))
        forbidden.add((x_center - 1, y_center + 1))
        forbidden.add((x_center - 1, y_center + 2))

        forbidden.add((x_center + 1, y_center))
        forbidden.add((x_center + 1, y_center - 2))
        forbidden.add((x_center + 2, y_center))
        forbidden.add((x_center + 3, y_center))
        forbidden.add((x_center + 3, y_center - 1))
        forbidden.add((x_center + 3, y_center - 2))
        forbidden.add((x_center + 2, y_center - 2))
        forbidden.add((x_center + 1, y_center + 1))
        forbidden.add((x_center + 1, y_center + 2))
        forbidden.add((x_center + 2, y_center + 2))
        forbidden.add((x_center + 3, y_center + 2))

    return grid, forbidden


def remove_wall(grid: list[list], x1: int, y1: int, x2: int, y2: int):

    dx = x2 - x1
    dy = y2 - y1

    if dx == 1:
        grid[y1][x1] &= ~E
        grid[y2][x2] &= ~W

    elif dx == -1:
        grid[y1][x1] &= ~W
        grid[y2][x2] &= ~E

    elif dy == 1:
        grid[y1][x1] &= ~S
        grid[y2][x2] &= ~N

    elif dy == -1:
        grid[y1][x1] &= ~N
        grid[y2][x2] &= ~S


def get_neighbors(
        x: int,
        y: int,
        width: int,
        height: int,
        visited: set,
        forbidden: set
        ) -> dict:

    neighbors = []

    if (
        (0 <= y + 1 < height)
        and (x, y + 1) not in visited
        and (x, y + 1) not in forbidden
    ):
        neighbors.append((x, y + 1))

    if (
        (0 <= x + 1 < width)
        and (x + 1, y) not in visited
        and (x + 1, y) not in forbidden
    ):
        neighbors.append((x + 1, y))

    if (
        (0 <= y - 1 < height)
        and (x, y - 1) not in visited
        and (x, y - 1) not in forbidden
    ):
        neighbors.append((x, y - 1))

    if (
        (0 <= x - 1 < width)
        and (x - 1, y) not in visited
        and (x - 1, y) not in forbidden
    ):
        neighbors.append((x - 1, y))

    return neighbors


def open_cell(
    grid: list[list], x: int, y: int, width: int, height
        ) -> list[list] | None:

    if (x != 0 and x != width - 1) and (y != 0 and y != height - 1):
        return None

    if y == 0:
        grid[y][x] &= ~N
    elif y == height - 1:
        grid[y][x] &= ~S
    elif x == 0:
        grid[y][x] &= ~W
    elif x == width - 1:
        grid[y][x] &= ~E

    return grid


def generate(
        grid: list[list],
        width: int,
        height: int,
        start_x: int,
        start_y: int,
        forbidden: set,
        seed: int | None = None
        ) -> list[list]:

    visited = set()
    stack = []

    x1 = int(start_x)
    y1 = int(start_y)

    if seed is not None:
        random.seed(seed)

    visited.add((x1, y1))
    stack.append((x1, y1))

    while stack:

        if get_neighbors(x1, y1, width, height, visited, forbidden):

            (x2, y2) = random.choice(
                get_neighbors(x1, y1, width, height, visited, forbidden)
            )
            remove_wall(grid, x1, y1, x2, y2)
            stack.append((x2, y2))
            visited.add((x2, y2))
            (x1, y1) = (x2, y2)

        else:
            stack.pop()
            if stack:
                (x1, y1) = stack[-1]

    return grid
