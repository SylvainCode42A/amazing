def create_grid(width: int, height: int) -> list[list]:
    grid = [[0xF] * width for _ in range(height)]
    return grid