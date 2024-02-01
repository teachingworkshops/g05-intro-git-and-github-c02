# Weapons class
from .Item import Item

class Weapon(Item):
    def __init__(self, 
                 name, 
                 description,
                 can_sell,
                 cost_value,
                 damage
                ):
        
        self.damage = damage
        self.description = description+"damage: "+" "+str(damage)+"hp"

        # Child class of item, can reference item attributes and functions
        super().__init__(name, self.description, can_sell, cost_value)


