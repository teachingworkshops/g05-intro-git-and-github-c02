# Backpack class
from .Item import Item

class Backpack(Item):
    def __init__(self, 
                 name, 
                 description, 
                 cost_value, 
                 storage_val
                ):
        
        self.storage_val = storage_val
        self.description = description +"\nstorage value: "+str(self.storage_val)+"\n"


        # List of objects in the characters backpack (not including maps and keys)
        self.backpack_storage = []

        # List of map objects
        self.map_storage = []

        # List of key objects
        self.key_storage = []

        # Child class of item, can reference item attributes and functions
        super().__init__(name, self.description, cost_value)