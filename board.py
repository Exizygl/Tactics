class Board:
    def __init__(self):
        self.tiles = [
            ["#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", "#"],
            ["#", ".", ".", ".", "#"],
            ["#", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#"],
        ]

    def is_walkable(self, x, y):
        return self.tiles[y][x] == "."