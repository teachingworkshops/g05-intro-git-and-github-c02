# Character class
from User_Objects.Backpack import Backpack

global STARTING_BACKPACK_STORAGE
STARTING_BACKPACK_STORAGE = 3

class MainCharacter:
    def __init__(self, name):
        self.name = name

        # Character starts with a backpack with the capacity of holding a maximum of three objects
        self.backpack = Backpack("backpack", "allows you to store items that you find", False, 50, STARTING_BACKPACK_STORAGE)

        # Starts with 50 coins?
        self.coin_storage = 50