from src.config_parser import parse_config, verify_dict
from src.maze_display import display_maze
from src.maze_generator import generate, open_cell, create_grid


N, E, S, W = 1, 2, 4, 8


def main() -> None:
    dict = parse_config("config.txt")

    if not verify_dict(dict):
        return
    else:
        width = int(dict["WIDTH"])
        height = int(dict["HEIGHT"])

        grid = create_grid(width, height)

        for line in grid:
            for cell in line:
                print(f"{cell:x}", end=" ")
            print()

        value = dict["ENTRY"]
        x_, y_ = value.split(",")
        x_start, y_start = int(x_), int(y_)
        grid = open_cell(grid, x_start, y_start, width, height)
        grid = generate(grid, width, height, x_start, y_start)

        exit = dict["EXIT"]
        x_, y_ = exit.split(",")
        xe, ye = int(x_), int(y_)

        open_cell(grid, xe, ye, width, height)

        print()
        print("-" * (width * 2), "\n")

        display_maze(grid, width, height)
        for line in grid:
            for cell in line:
                print(f"{cell:x}", end=" ")
            print()


if __name__ == "__main__":
    main()
