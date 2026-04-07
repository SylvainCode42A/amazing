def remove_wall(grid: list[list]):
    for line in grid:
        for cell in line:
            print(f"{cell:x}", end="")
        print()