# Character class
from User_Objects.Backpack import Backpack

global STARTING_BACKPACK_STORAGE
STARTING_BACKPACK_STORAGE = 3

class MainCharacter:
    def __init__(self, name):
        self.name = name
        self.health_points = 100

        # Character starts with a backpack with the capacity of holding a maximum of three objects
        self.backpack = Backpack("backpack", "allows you to store items that you find", False, 50, STARTING_BACKPACK_STORAGE)

        # Starts with 50 coins
        self.coin_storage = 50

        # Dictionary of the armor a main charact has
        self.armor_dict = {
            "head": "", 
            "chest": "", 
            "leg": "",
            "boot": "" 
            }
        
        self.weapon = ("none", 0)
    
    # Updates the number of the health points the player has based on the added armor
    def update_health_points(self, new_armor):
        old_armor = self.armor_dict[new_armor.armor_type]
        # Subtracts the added protectin of the old armor
        self.health_points = self.health_points - self.armor_dict[old_armor.armor_type].protection_value
        # Replaces the old armor with the new armor
        self.armor_dict[new_armor.armor_type] = new_armor

        # Updates the health points with the new armor
        self.health_points = self.health_points + self.armor_dict[new_armor.armor_type].protection_value

    def update_weapon(self, new_weapon):
        self.weapon=(new_weapon.get_name(), new_weapon.get_damage())

    def get_weapon(self):
        return self.weapon
