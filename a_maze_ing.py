from src.config_parser import parse_config, verify_dict
from src.maze_display import display_maze
from src.maze_generator import generate, open_cell, create_grid
from src.maze_solver import find_exit
from src.maze_writer import write_maze


N, E, S, W = 1, 2, 4, 8


def main() -> None:
    dict = parse_config("config.txt")

    if not verify_dict(dict):
        return
    else:
        width = int(dict["WIDTH"])
        height = int(dict["HEIGHT"])

        grid, forbidden = create_grid(width, height)

        value = dict["ENTRY"]
        x_, y_ = value.split(",")
        x_start, y_start = int(x_), int(y_)
        grid = open_cell(grid, x_start, y_start, width, height)
        grid = generate(grid, width, height, x_start, y_start, forbidden)

        exit = dict["EXIT"]
        x_, y_ = exit.split(",")
        x_exit, y_exit = int(x_), int(y_)

        open_cell(grid, x_exit, y_exit, width, height)

        print("\n")

        path, direction = find_exit(
            grid, width, height, (x_start, y_start), (x_exit, y_exit))
        display_maze(
            grid, (x_start, y_start), (x_exit, y_exit), path, forbidden)
        write_maze(
            grid,
            (x_start, y_start),
            (x_exit, y_exit),
            direction,
            dict["OUTPUT_FILE"])

        print("\n")


if __name__ == "__main__":
    main()
