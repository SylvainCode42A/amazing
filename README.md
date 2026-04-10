*This project has been created as part of the 42 curriculum by slidriss, bgranier.*

# A-Maze-ing

## Description

A-Maze-ing is a maze generator written in Python. It takes a configuration file, generates a random maze using a DFS backtracker algorithm, and writes the result to an output file using a hexadecimal wall encoding. The maze is displayed in the terminal with ASCII rendering and supports real-time user interaction. The generation logic is also available as a standalone pip-installable module.

---

## Instructions

### Requirements

- Python 3.10 or later
- pip

### Installation

```bash
make install
```

### Run

```bash
python3 a_maze_ing.py config.txt
```

### Other commands

```bash
make run          # run the project
make debug        # run with pdb
make lint         # flake8 + mypy
make lint-strict  # mypy --strict
make clean        # remove __pycache__, .mypy_cache
```

---

## Configuration file format

One `KEY=VALUE` pair per line. Lines starting with `#` are comments and are ignored.

**Mandatory keys:**

| Key | Description | Example |
|---|---|---|
| `WIDTH` | Number of cells horizontally | `WIDTH=20` |
| `HEIGHT` | Number of cells vertically | `HEIGHT=15` |
| `ENTRY` | Entry coordinates `x,y` | `ENTRY=0,0` |
| `EXIT` | Exit coordinates `x,y` | `EXIT=19,14` |
| `OUTPUT_FILE` | Output file path | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | Perfect maze? `True` or `False` | `PERFECT=True` |

**Optional keys:**

| Key | Description | Example |
|---|---|---|
| `SEED` | Integer seed for reproducibility | `SEED=42` |

**Example:**

```ini
# Maze configuration
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
```

---

## Maze generation algorithm

The maze is generated using a **randomized DFS backtracker** (recursive backtracker).

**How it works:**

1. Start from the entry cell and mark it as visited.
2. Randomly pick an unvisited neighbor.
3. Remove the wall between the current cell and the chosen neighbor.
4. Move to that neighbor and repeat.
5. If no unvisited neighbor exists, backtrack to the previous cell.
6. Repeat until all cells have been visited.

**Why this algorithm:**

- Produces perfect mazes by construction, which satisfies `PERFECT=True` with no extra work.
- Guarantees full connectivity with no isolated cells.
- Simple to implement and easy to debug.
- Reproducibility via seed is trivially supported by seeding Python's `random` module.
- When `PERFECT=False`, a post-processing step randomly removes walls to create loops.

**The "42" pattern:**

Before generation, a set of cells is marked as forbidden. The DFS never visits them, leaving them fully walled. When rendered, they form a visible "42" in the center of the maze. If the maze is too small (WIDTH < 9 or HEIGHT < 7), the pattern is omitted and a warning is printed.

---

## Output file format

Each cell is encoded as a single hexadecimal digit where each bit represents a wall:

| Bit | Direction |
|---|---|
| 0 (LSB) | North |
| 1 | East |
| 2 | South |
| 3 | West |

Bit set to `1` means the wall is closed, `0` means open. Cells are stored row by row, one row per line. After an empty line, three additional lines follow: entry coordinates, exit coordinates, and the shortest path as a sequence of `N`, `E`, `S`, `W`.

**Example:**

```
c39393
96aaea
c56c52
955796
8553ab
c57c42

0,0
5,5
ESWSEENNESSEESWSSE
```

---

## Visual representation

The maze is rendered in the terminal using `+`, `-`, `|`. The entry cell is marked `E` and the exit cell is marked `X`.

**Controls:**

| Key | Action |
|---|---|
| `p` | Show / hide the shortest path |
| `r` | Regenerate a new maze |
| `c` | Cycle through wall colors |
| `q` | Quit |

---

## Reusable module

The maze generation logic is packaged as a pip-installable module named `mazegen`. The package files are at the root of the repository:

```
mazegen-1.0.0-py3-none-any.whl
mazegen-1.0.0.tar.gz
```

**Installation:**

```bash
pip install mazegen-1.0.0-py3-none-any.whl
```

**Rebuild from source:**

```bash
pip install build
python -m build
pip install dist/mazegen-1.0.0-py3-none-any.whl
```

**Basic usage:**

```python
from mazegen import MazeGenerator

maze = MazeGenerator(height=10, width=10)

grid = maze.get_grid()   # list[list[int]]
path = maze.get_path()   # list[tuple[int, int]]
```

**Custom parameters:**

```python
maze = MazeGenerator(
    height=15,
    width=20,
    start=(0, 0),
    end=(19, 14),
    seed=42
)
```

**Available methods:**

| Method | Returns | Description |
|---|---|---|
| `get_grid()` | `list[list[int]]` | Full grid — each int encodes walls as bits (N=0, E=1, S=2, W=3) |
| `get_path()` | `list[tuple[int, int]]` | Shortest path from entry to exit as `(x, y)` tuples |

---

## Team and project management

### Roles

| Member | Responsibilities |
|---|---|
| slidriss | Maze generation, config parser, output writer, Makefile, packaging |
| bgranier | Terminal display, BFS solver, main entry point, reusable module, README |

### Planning

The project was split into four phases: configuration parsing, maze generation, solving and file output, display and packaging. The first two phases were completed ahead of schedule, giving extra time to polish the display and the reusable module.

### What worked well

- Splitting the project into clearly separated modules made parallel work easy.
- Using a `forbidden` set for the "42" pattern integrated naturally with the DFS.
- The DFS backtracker was straightforward to implement and debug.

### What could be improved

- `make_imperfect` only removes horizontal walls, limiting variety in imperfect mazes.
- A graphical backend (MLX) would improve the experience for larger mazes.
- Entry/exit bounds validation could be more thorough in `verify_dict`.

### Tools used

- VSCode for development
- pytest for local testing
- mypy and flake8 for static analysis
- AI assistance (see Resources)

---

## Resources

- [Maze generation algorithms — Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Recursive backtracker — jamisbuck.org](https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracker)
- [Python packaging guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [flake8 documentation](https://flake8.pycqa.org/)
- [mypy documentation](https://mypy.readthedocs.io/)
- [readchar library](https://pypi.org/project/readchar/)

### AI usage

AI tools were used for the following tasks:

- Getting an initial explanation of the DFS backtracker and how to apply it to a grid.
- Suggesting the bit-encoding scheme for walls.
- Helping debug wall coherence issues between neighboring cells.
- Getting a starting template for `pyproject.toml`.

All AI-generated content was reviewed, tested, and adapted by both team members before being integrated into the project.