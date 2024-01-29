# Weapons class
from .Item import Item

class Weapon(Item):
    def __init__(self, 
                 name, 
                 description,
                 cost_value,
                 damage
                ):
        
        self.damage = damage
        self.description = description+"\ndamage: "+str(damage)+"hp\n"

        # Child class of item, can reference item attributes and functions
        super().__init__(name, self.description, cost_value)


