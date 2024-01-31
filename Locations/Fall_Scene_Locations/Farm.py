from Locations import Locations
from User_Objects.Weapon import Weapon
from User_Objects.Armor import Armor
from User_Objects.Item import Item

global SWORD_VALUE
SWORD_VALUE = 25

global SWORD_DAMAGE
SWORD_DAMAGE = 50

global COIN_AMOUNT
COIN_AMOUNT = 25

global CHEST_PLATE_VALUE
CHEST_PLATE_VALUE = 50

global CHEST_PLATE_PROTECTION_VALUE
CHEST_PLATE_PROTECTION_VALUE = 75

class Farm(Locations):
    def __init__(self, name, discovered):
        self.name = name
        self.discovered = discovered # Boolean

        sword = Weapon("Sword", "A weapon that deals damage to enemies.", True, SWORD_VALUE, SWORD_DAMAGE)
        gold_coins = Item("Gold Coins", "The currency used to buy and sell items.", False, COIN_AMOUNT)
        self.wood_chest = [sword, gold_coins]


        chest_plate = Armor("Chestplate", "Adds protection to any danger that approaches", True, CHEST_PLATE_VALUE, "chest", CHEST_PLATE_PROTECTION_VALUE)
        self.horse_stable_wall = [chest_plate]

        # Child class of item, can reference item attributes and functions
        super().__init__(name, discovered)

    def display_backpack_items(self, main_character):
        print("")

    def display_locations(self):
        print("")

    def display_sublocations(self):
        print("")

    def farmer_dialogue(self):
        print("Hello there!\n")

    def location_scene(self, main_character):
        print("You have successfully traveled to the farm.")
        print("Available commands:")
        action = input("[0]Approach farmer\n['i']Inspect sublocations\n['b']Open backpack\n['q']Leave location")
        while action != "q":
            if action == "0":
                self.farmer_dialogue()
            elif action == "i":
                self.display_sublocations()
            elif action == "b":
                self.display_backpack_items(main_character)

            
