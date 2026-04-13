import random

N, E, S, W = 1, 2, 4, 8


def create_grid(width: int, height: int) -> tuple[list[list[int]],
                                                  set[tuple[int, int]]]:
    """Create an initial fully-walled grid and define the '42' pattern.

    All cells start with all 4 walls closed (0xF). If the maze is large
    enough, a set of forbidden cells forming the '42' pattern is computed
    and returned. Forbidden cells are never visited during generation.

    Args:
        width: Number of columns in the maze.
        height: Number of rows in the maze.

    Returns:
        A tuple of:
            - grid: 2D list of integers, all initialised to 0xF.
            - forbidden: Set of (x, y) cells reserved for the '42' pattern.
    """
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
    """Remove the wall between two adjacent cells.

    Updates both cells symmetrically to keep the grid coherent.

    Args:
        grid: 2D list of integers encoding walls per cell.
        x1: Column of the first cell.
        y1: Row of the first cell.
        x2: Column of the second cell.
        y2: Row of the second cell.
    """
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
    """Return unvisited, non-forbidden neighbours of a cell.

    Args:
        x: Column of the current cell.
        y: Row of the current cell.
        width: Number of columns in the maze.
        height: Number of rows in the maze.
        visited: Set of already visited (x, y) cells.
        forbidden: Set of cells that must not be visited.

    Returns:
        List of (x, y) coordinates of valid neighbour cells.
    """
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
    """Open the external wall of a border cell to create an entry or exit.

    Does nothing if the cell is not on the maze border.

    Args:
        grid: 2D list of integers encoding walls per cell.
        x: Column of the cell.
        y: Row of the cell.
        width: Number of columns in the maze.
        height: Number of rows in the maze.

    Returns:
        The updated grid, or None if the cell is not on the border.
    """

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
    """Generate a perfect maze using a randomized DFS backtracker.

    Starts from the given cell and carves passages until all reachable
    cells have been visited. Forbidden cells are never entered.

    Args:
        grid: 2D list of integers encoding walls per cell.
        width: Number of columns in the maze.
        height: Number of rows in the maze.
        start_x: Column of the starting cell.
        start_y: Row of the starting cell.
        forbidden: Set of (x, y) cells that must not be visited.
        seed: Optional integer seed for reproducible generation.

    Returns:
        The updated grid with walls removed to form the maze.
    """

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
    forbidden: set[tuple[int, int]],
    seed: int | None = None
) -> list[list[int]]:
    """Introduce loops into the maze by randomly removing walls.

    Removes approximately 10% of the total walls. Skips forbidden cells
    and cancels any removal that would create a 3x3 open area.

    Args:
        grid: 2D list of integers encoding walls per cell.
        width: Number of columns in the maze.
        height: Number of rows in the maze.
        forbidden: Set of (x, y) cells that must not be modified.
        seed: Optional integer seed for reproducible generation.

    Returns:
        The updated grid with additional walls removed.
    """

    if seed is not None:
        random.seed(seed)

    break_wall = (width * height) // 10
    attempts = 0

    while break_wall > 0 and attempts < width * height * 10:
        x = random.randint(0, width - 2)
        y = random.randint(0, height - 1)
        attempts += 1

        if (x, y) in forbidden or (x + 1, y) in forbidden:
            continue

        grid[y][x] &= ~E
        grid[y][x + 1] &= ~W

        if _has_3x3_open(grid, x, y, width, height):
            grid[y][x] |= E
            grid[y][x + 1] |= W
        else:
            break_wall -= 1

    return grid


def _has_3x3_open(
    grid: list[list[int]],
    cx: int,
    cy: int,
    width: int,
    height: int
) -> bool:
    """Check whether a 3x3 fully open area exists near a given cell.

    Args:
        grid: 2D list of integers encoding walls per cell.
        cx: Column of the recently modified cell.
        cy: Row of the recently modified cell.
        width: Number of columns in the maze.
        height: Number of rows in the maze.

    Returns:
        True if a 3x3 open area is detected, False otherwise.
    """
    for y in range(max(0, cy - 2), min(height - 2, cy + 2)):
        for x in range(max(0, cx - 2), min(width - 2, cx + 2)):
            all_open = True
            for dy in range(3):
                for dx in range(3):
                    nx, ny = x + dx, y + dy
                    if nx >= width or ny >= height:
                        all_open = False
                        break
                    if dy < 2 and (grid[ny][nx] & S):
                        all_open = False
                    if dx < 2 and (grid[ny][nx] & E):
                        all_open = False
                if not all_open:
                    break
            if all_open:
                return True
    return False
