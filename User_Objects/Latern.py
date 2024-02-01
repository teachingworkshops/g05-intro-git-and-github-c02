from .Item import Item

class Latern(Item):
    def __init__(self, 
                 name,
                 description, 
                 cost_value
                ):

        # Child class of item, can reference item attributes and functions
        super().__init__(name, description, cost_value)