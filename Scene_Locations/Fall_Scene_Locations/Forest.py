import Locations

class Forest(Locations):
    def __init__(self, name, discovered):
        self.name = name
        self.discovered = discovered

        # Child class of item, can reference item attributes and functions
        super().__init__(name, discovered)

    