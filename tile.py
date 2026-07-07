class Tile:
    def __init__(self, symbol):
        self.symbol = symbol

    def movement_cost(self, unit):
        return 1

    def defense_bonus(self, unit):
        return 0

    def avoid_bonus(self, unit):
        return 0

    def can_enter(self, unit):
        return true