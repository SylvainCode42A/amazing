N, E, S, W = 1, 2, 4, 8


def choices_to_go(
        grid: list[list],
        x: int,
        y: int,
        height: int,
        width: int
        ) -> dict[str, tuple]:

    choices = {}

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
        grid: list[list],
        width: int,
        height: int,
        start: int,
        end: int
        ) -> list[tuple]:

    queue = [start]
    came_from = {start: None}

    while queue:
        x, y = queue.pop(0)

        if (x, y) == end:
            break

        for (x2, y2) in choices_to_go(grid, x, y, height, width).values():
            if (x2, y2) not in came_from:
                came_from[(x2, y2)] = (x, y)
                queue.append((x2, y2))

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse()

    direction = []
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
