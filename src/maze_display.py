def display_maze(
    maze: list[list],
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    path: list[tuple[int, int]],
    forbidden: set,
    color: int
) -> None:

    COLORS = [
        "\033[0m",   # blanc
        "\033[31m",  # rouge
        "\033[32m",  # vert
        "\033[34m",  # bleu
        "\033[33m",  # jaune
    ]

    H, W = len(maze), len(maze[0])
    NORTH, EAST, SOUTH, WEST = 0b0001, 0b0010, 0b0100, 0b1000

    lines = []

    for row in range(H):
        top = ''
        for col in range(W):
            top += COLORS[0] + '+'
            top += COLORS[color] + '---' if (maze[row][col] & NORTH) else COLORS[0] + '   '
        top += COLORS[0] + '+'
        lines.append(top)

        mid = COLORS[0] + ''
        for col in range(W):
            mid += COLORS[color] + '|' if (maze[row][col] & WEST) else COLORS[0] + ' '
            if (col, row) == entry:
                mid += COLORS[0] + ' E '
            elif (col, row) == exit_pos:
                mid += COLORS[0] + ' X '
            elif (col, row) in path:
                mid += COLORS[0] + ' . '
            elif (col, row) in forbidden:
                mid += COLORS[0] + ' # '
            else:
                mid += COLORS[0] + '   '
        mid += COLORS[color] + '|' if (maze[row][W - 1] & EAST) else COLORS[0] + ' '
        lines.append(mid)

    bot = COLORS[0] + ''
    for col in range(W):
        bot += COLORS[0] + '+'
        bot += COLORS[color] + '---' if (maze[H - 1][col] & SOUTH) else COLORS[0] + '   '
    bot += COLORS[0] + '+'
    lines.append(bot)

    print('\n'.join(lines))
