from src.config_parser import parse_config, verify_dict
from src.maze_display import display_maze
from src.maze_generator import generate, open_cell, create_grid, make_imperfect
from src.maze_solver import find_exit
from src.maze_writer import write_maze
import readchar
import sys


N, E, S, W = 1, 2, 4, 8


def main() -> None:
    """Entry point of the maze generator program.

    Parses the configuration file, generates the maze, writes it to the
    output file, and starts an interactive terminal display loop.

    Controls:
        p: Show or hide the shortest path.
        r: Regenerate a new maze with the same configuration.
        c: Cycle through wall colours.
        q: Quit the program.
    """
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 a_maze_ing.py config.txt")
            return
        config = parse_config(sys.argv[1])
    except Exception as e:
        print(e)
        return

    try:
        verify_dict(config)
    except Exception as e:
        print(e)
        return

    width = int(config["WIDTH"])
    height = int(config["HEIGHT"])

    if width <= 1 or height <= 1:
        print("Too small only one cell")
        return

    grid, forbidden = create_grid(width, height)

    if not forbidden:
        print("Warning: maze too small for '42' pattern.")

    value = config["ENTRY"]
    x_, y_ = value.split(",")
    x_start, y_start = int(x_), int(y_)

    if not (x_start == 0
            or x_start == width - 1
            or y_start == 0
            or y_start == height - 1):
        print("Error: ENTRY must be on the border of the maze.")
        return

    if "SEED" in config:
        try:
            seed = int(config["SEED"])
        except ValueError:
            seed = None
    else:
        seed = None

    exit_coord = config["EXIT"]
    x_, y_ = exit_coord.split(",")
    x_exit, y_exit = int(x_), int(y_)

    if not (x_exit == 0
            or x_exit == width - 1
            or y_exit == 0
            or y_exit == height - 1):
        print("Error: EXIT must be on the border of the maze.")
        return

    grid = generate(
                grid,
                width,
                height,
                x_start,
                y_start,
                forbidden,
                seed
                )

    open_cell(
        grid,
        x_start,
        y_start,
        width,
        height
        )

    open_cell(
        grid,
        x_exit,
        y_exit,
        width,
        height
        )

    if config["PERFECT"] == "False":
        grid = make_imperfect(
            grid,
            width,
            height,
            forbidden,
            seed
            )

    path, direction = find_exit(
        grid,
        width,
        height,
        (x_start, y_start),
        (x_exit, y_exit)
        )

    write_maze(
        grid,
        (x_start, y_start),
        (x_exit, y_exit),
        direction,
        config["OUTPUT_FILE"]
        )

    show_path = False
    color = 0

    try:
        while True:
            print("\033[H\033[J", end="")
            display_maze(
                    grid,
                    (x_start, y_start),
                    (x_exit, y_exit),
                    path if show_path else [],
                    forbidden,
                    color
                    )

            print("\np = show/hide path | r = regenerate |"
                  " c = change color | q = quit")

            key = readchar.readkey()

            if key == 'q':
                return

            elif key == 'p':
                show_path = not show_path

            elif key == 'r':

                grid, forbidden = create_grid(width, height)

                grid = generate(
                    grid,
                    width,
                    height,
                    x_start,
                    y_start,
                    forbidden,
                    seed
                    )

                open_cell(
                    grid,
                    x_start,
                    y_start,
                    width,
                    height
                    )

                open_cell(
                    grid,
                    x_exit,
                    y_exit,
                    width,
                    height
                    )

                if config["PERFECT"] == "False":
                    grid = make_imperfect(
                        grid,
                        width,
                        height,
                        forbidden,
                        seed
                        )

                path, direction = find_exit(
                    grid,
                    width,
                    height,
                    (x_start, y_start),
                    (x_exit, y_exit)
                    )

                write_maze(
                    grid,
                    (x_start, y_start),
                    (x_exit, y_exit),
                    direction,
                    config["OUTPUT_FILE"]
                    )

            elif key == 'c':
                if color + 1 < 5:
                    color += 1
                else:
                    color = 0

    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
