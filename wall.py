class Wall(Tile):
    def __init__(self):
        super().__init__("#")

    def can_enter(self, unit):
        return False