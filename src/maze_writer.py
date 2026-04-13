def write_maze(
    grid: list[list[int]],
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    direction: list[str],
    filename: str
) -> None:
    """Write the maze to a file in hexadecimal format.

    Each cell is encoded as a single hex digit. After the grid,
    an empty line is followed by the entry coordinates, exit
    coordinates, and the shortest path as a sequence of N/E/S/W.

    Args:
        grid: 2D list of integers encoding walls per cell.
        entry: (x, y) coordinates of the maze entry.
        exit_pos: (x, y) coordinates of the maze exit.
        direction: List of direction characters ('N', 'E', 'S', 'W').
        filename: Path to the output file.
    """

    with open(filename, "w") as f:

        for line in grid:
            for cell in line:
                f.write(hex(cell)[2:])
            f.write("\n")

        f.write("\n")
        f.write(f"{entry[0]},{entry[1]}\n")
        f.write(f"{exit_pos[0]},{exit_pos[1]}\n")

        for dir in direction:
            f.write(dir)
        f.write("\n")
