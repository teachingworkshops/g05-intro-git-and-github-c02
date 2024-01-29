# Armor class
from .Item import Item

class Armor(Item):
    def __init__(self, 
                 name, 
                 description, 
                 cost_value,
                 armor_type, 
                 protection_value
                ):
        
        self.description = description +"\narmor type: "+armor_type+"\nprotection value: "+str(protection_value)+"hp\n"
        self.armor_type = armor_type
        self.protection_value = protection_value

        # Child class of item, can reference item attributes and functions
        super().__init__(name, self.description, cost_value)