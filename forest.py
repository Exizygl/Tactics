class Forest(tile):
    def __init__(self):
        super().__init__(".")

    def movement_cost(self, unit):
        if unit.movement_type == "cav":
            return 3; 
        if unit.movement_type == "flier":
            return 3; 
        return 2

    def defense_bonus(self, unit):
        if unit.movement_type == "flier":
            return 0; 
        return 1

    def avoid_bonus(self, unit):
        if unit.movement_type == "flier":
            return 0; 
        return 10

    def can_enter(self, unit):
        return true