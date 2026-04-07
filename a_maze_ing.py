import sys
sys.path.append("src")

from config_parser import parse_config, verify_dict
from maze_display import create_grid
from maze_generator import remove_wall


def main() -> None:
    dict = parse_config("config.txt")

    if not verify_dict(dict):
        return
    else:
        width = int(dict["WIDTH"])
        height = int(dict["HEIGHT"])

        grid = create_grid(width, height)
        remove_wall(grid)

main()