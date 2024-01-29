# Character class
from User_Objects.Backpack import backpack

class main_character:
    def __init__(self, name):
        self.name = name

        # Character starts with a backpack with the capacity of holding a maximum of three objects
        self.backpack = backpack(3)