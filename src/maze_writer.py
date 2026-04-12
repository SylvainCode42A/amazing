def write_maze(
    grid: list[list[int]],
    entry: tuple[int, int],
    exit_pos: tuple[int, int],
    direction: list[str],
    filename: str
) -> None:

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
