def display_maze(
    maze: list[list],
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    path: list[tuple[int, int]],
    forbidden: set
) -> None:
    H, W = len(maze), len(maze[0])
    NORTH, EAST, SOUTH, WEST = 0b0001, 0b0010, 0b0100, 0b1000

    lines = []

    for row in range(H):
        top = ''
        for col in range(W):
            top += '+'
            top += '---' if (maze[row][col] & NORTH) else '   '
        top += '+'
        lines.append(top)

        mid = ''
        for col in range(W):
            mid += '|' if (maze[row][col] & WEST) else ' '
            if (col, row) == entry:
                mid += ' E '
            elif (col, row) == exit_pos:
                mid += ' X '
            elif (col, row) in path:
                mid += ' . '
            elif (col, row) in forbidden:
                mid += ' # '
            else:
                mid += '   '
        mid += '|' if (maze[row][W - 1] & EAST) else ' '
        lines.append(mid)

    bot = ''
    for col in range(W):
        bot += '+'
        bot += '---' if (maze[H - 1][col] & SOUTH) else '   '
    bot += '+'
    lines.append(bot)

    print('\n'.join(lines))
