from src.maze_generator import generate, create_grid, open_cell
from src.maze_solver import find_exit


class MazeGenerator():
    def __init__(
        self,
        height: int,
        width: int,
        start: tuple[int, int] = (0, 0),
        end: tuple[int, int] | None = None,
        seed: int | None = None
    ) -> None:
        self.height = height
        self.width = width
        self.start = start
        self.end = end if end else (width - 1, height - 1)
        self.seed = seed
        self.grid, self.forbidden = create_grid(width, height)
        self.path = []
        self.direction = []
        x_start, y_start = self.start
        x_exit, y_exit = self.end
        self.grid = generate(
            self.grid,
            self.width,
            self.height,
            x_start,
            y_start,
            self.forbidden,
            self.seed
            )
        open_cell(self.grid, x_start, y_start, self.width, self.height)
        open_cell(self.grid, x_exit, y_exit, self.width, self.height)
        self.path, self.direction = find_exit(
                    self.grid,
                    self.width,
                    self.height,
                    (x_start, y_start),
                    (x_exit, y_exit)
                    )

    def get_grid(self):
        return self.grid

    def get_path(self):
        return self.path
