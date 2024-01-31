# The item class is the parent to all of the other user objects

class Item:
    def __init__(self, name: str, description: str, can_sell: bool, cost_value: int):
        self.name = name
        self.description = description
        self.cost_value = cost_value
        self.can_sell = can_sell # True = can sell, False = cannot sell