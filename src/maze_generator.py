import random

N, E, S, W = 1, 2, 4, 8


def create_grid(width: int, height: int) -> tuple[list[list[int]],
                                                  set[tuple[int, int]]]:
    grid: list[list[int]] = [[0xF] * width for _ in range(height)]
    forbidden: set[tuple[int, int]] = set()

    if width < 9 or height < 7:
        return grid, forbidden

    x_center, y_center = width // 2, height // 2

    forbidden.update({
        (x_center - 1, y_center),
        (x_center - 2, y_center),
        (x_center - 3, y_center),
        (x_center - 1, y_center - 2),
        (x_center - 3, y_center - 1),
        (x_center - 3, y_center - 2),
        (x_center - 1, y_center - 1),
        (x_center - 1, y_center + 1),
        (x_center - 1, y_center + 2),

        (x_center + 1, y_center),
        (x_center + 1, y_center - 2),
        (x_center + 2, y_center),
        (x_center + 3, y_center),
        (x_center + 3, y_center - 1),
        (x_center + 3, y_center - 2),
        (x_center + 2, y_center - 2),
        (x_center + 1, y_center + 1),
        (x_center + 1, y_center + 2),
        (x_center + 2, y_center + 2),
        (x_center + 3, y_center + 2),
    })

    return grid, forbidden


def remove_wall(
    grid: list[list[int]],
    x1: int,
    y1: int,
    x2: int,
    y2: int
) -> None:
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
    visited: set[tuple[int, int]],
    forbidden: set[tuple[int, int]]
) -> list[tuple[int, int]]:
    neighbors: list[tuple[int, int]] = []

    candidates = [
        (x, y + 1),
        (x + 1, y),
        (x, y - 1),
        (x - 1, y),
    ]

    for nx, ny in candidates:
        if (
            0 <= nx < width
            and 0 <= ny < height
            and (nx, ny) not in visited
            and (nx, ny) not in forbidden
        ):
            neighbors.append((nx, ny))

    return neighbors


def open_cell(
    grid: list[list[int]],
    x: int,
    y: int,
    width: int,
    height: int
) -> list[list[int]] | None:

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
    grid: list[list[int]],
    width: int,
    height: int,
    start_x: int,
    start_y: int,
    forbidden: set[tuple[int, int]],
    seed: int | None = None
) -> list[list[int]]:

    if seed is not None:
        random.seed(seed)

    visited: set[tuple[int, int]] = set()
    stack: list[tuple[int, int]] = []

    x1, y1 = start_x, start_y

    visited.add((x1, y1))
    stack.append((x1, y1))

    while stack:
        neighbors = get_neighbors(x1, y1, width, height, visited, forbidden)

        if neighbors:
            x2, y2 = random.choice(neighbors)
            remove_wall(grid, x1, y1, x2, y2)

            stack.append((x2, y2))
            visited.add((x2, y2))
            x1, y1 = x2, y2
        else:
            stack.pop()
            if stack:
                x1, y1 = stack[-1]

    return grid


def make_imperfect(
    grid: list[list[int]],
    width: int,
    height: int,
    seed: int | None = None
) -> list[list[int]]:

    if seed is not None:
        random.seed(seed)

    break_wall = (width * height) // 10

    for _ in range(break_wall):
        x = random.randint(0, width - 2)
        y = random.randint(0, height - 1)

        grid[y][x] &= ~E
        grid[y][x + 1] &= ~W

    return grid
