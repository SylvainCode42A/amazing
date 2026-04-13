N, E, S, W = 1, 2, 4, 8


def choices_to_go(
        grid: list[list[int]],
        x: int,
        y: int,
        height: int,
        width: int
        ) -> dict[str, tuple[int, int]]:
    """Return accessible neighbours of a cell based on open walls.

    Args:
        grid: 2D list of integers encoding walls per cell.
        x: Column index of the current cell.
        y: Row index of the current cell.
        height: Number of rows in the maze.
        width: Number of columns in the maze.

    Returns:
        A dict mapping direction names to (x, y) neighbour coordinates.
    """

    choices: dict[str, tuple[int, int]] = {}

    if x + 1 < width and not (grid[y][x] & E):
        choices["right"] = (x + 1, y)

    if x - 1 >= 0 and not (grid[y][x] & W):
        choices["left"] = (x - 1, y)

    if y - 1 >= 0 and not (grid[y][x] & N):
        choices["up"] = (x, y - 1)

    if y + 1 < height and not (grid[y][x] & S):
        choices["down"] = (x, y + 1)

    return choices


def find_exit(
        grid: list[list[int]],
        width: int,
        height: int,
        start: tuple[int, int],
        end: tuple[int, int]
        ) -> tuple[list[tuple[int, int]], list[str]]:
    """Find the shortest path from start to end using BFS.

    Args:
        grid: 2D list of integers encoding walls per cell.
        width: Number of columns in the maze.
        height: Number of rows in the maze.
        start: (x, y) coordinates of the entry cell.
        end: (x, y) coordinates of the exit cell.

    Returns:
        A tuple of:
            - path: List of (x, y) coordinates from start to end.
            - direction: List of direction characters ('N', 'E', 'S', 'W').
    """

    queue: list[tuple[int, int]] = [start]
    came_from: dict[tuple[int, int], tuple[int, int] | None] = {start: None}

    while queue:
        x, y = queue.pop(0)

        if (x, y) == end:
            break

        for (x2, y2) in choices_to_go(grid, x, y, height, width).values():
            if (x2, y2) not in came_from:
                came_from[(x2, y2)] = (x, y)
                queue.append((x2, y2))

    path: list[tuple[int, int]] = []
    current: tuple[int, int] | None = end

    while current is not None:
        path.append(current)
        current = came_from.get(current)

    path.reverse()

    direction: list[str] = []
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]

        if x2 == x1 + 1:
            direction.append("E")
        elif x2 == x1 - 1:
            direction.append("W")
        elif y2 == y1 + 1:
            direction.append("S")
        elif y2 == y1 - 1:
            direction.append("N")

    return path, direction
