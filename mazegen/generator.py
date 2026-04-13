from src.maze_generator import generate, create_grid, open_cell
from src.maze_solver import find_exit


class MazeGenerator():
    """Standalone maze generator usable as a pip-installable module.

    Generates a perfect maze using a randomized DFS backtracker.
    Provides access to the grid structure and the shortest solution path.

    Example:
        maze = MazeGenerator(height=10, width=10)
        grid = maze.get_grid()
        path = maze.get_path()

    Args:
        height: Number of rows in the maze.
        width: Number of columns in the maze.
        start: (x, y) coordinates of the entry cell. Defaults to (0, 0).
        end: (x, y) coordinates of the exit cell.
            Defaults to (width - 1, height - 1).
        seed: Integer seed for reproducible generation. Defaults to None.
    """

    def __init__(
        self,
        height: int,
        width: int,
        start: tuple[int, int] = (0, 0),
        end: tuple[int, int] | None = None,
        seed: int | None = None
    ) -> None:
        """Initialise and generate the maze."""
        self.height = height
        self.width = width
        self.start = start
        self.end = end if end else (width - 1, height - 1)
        self.seed = seed
        self.grid, self.forbidden = create_grid(width, height)
        self.path: list[tuple[int, int]] = []
        self.direction: list[str] = []
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

    def get_grid(self) -> list[list[int]]:
        """Return the maze grid.

        Returns:
            2D list where each integer encodes the walls of a cell
            as bits: N=1, E=2, S=4, W=8. A set bit means the wall
            is closed.
        """
        return self.grid

    def get_path(self) -> list[tuple[int, int]]:
        """Return the shortest path from entry to exit.

        Returns:
            List of (x, y) coordinates from start to end inclusive.
        """
        return self.path
