# Fall scene for the story

from User_Objects.Armor import Armor
from User_Objects.Key import Key
from User_Objects.Weapon import Weapon
from User_Objects.Backpack import Backpack

from Characters.Main_Character import MainCharacter
from Characters.Merchant_Character import Merchant

from Scene_Locations.Fall_Scene_Locations.Farm import Farm
from Scene_Locations.Fall_Scene_Locations.Forest import Forest
from Scene_Locations.Fall_Scene_Locations.Great_Pumpkin import Great_Pumpkin

class fall_scene:
    def __init__(self):
        self.locations = []
    # Runs the fall scene
    def run_scene(self, traveler: MainCharacter):
        print("Welcome to the Fall Scene!\n")
        print("To begin there will be a traveling merchant at the start of each scene. Would you like to speak with the merchant?\n")
        while True: 
            print(f"You currently have: {traveler.coin_storage} coins\n")
            talk_to_merchant = input("Enter ['y'] for yes or ['n'] for no\n")
            if talk_to_merchant == 'y':
                self.merchant_scene(traveler)
                break # Ends while loop
            elif talk_to_merchant == 'n':
                break # Ends while loop
            else:
                print("Please answer with 'y' or 'n.\n")

        self.travel_function(traveler)

    # Tests the merchants dialogue and function of buying from the merchant 
    def merchant_scene(self, traveler):
        # Creates items for the character to buy
        axe = Weapon("Battle Axe", "A weapon that deals damage to enemies.", True, 25, 35)
        backpack_object = Backpack("Backpack", "Carries items that you pick up", True, 50, 5)
        helmet = Armor("Helmet", "Adds protection to any danger that approaches", True, 35, "head", 50)

        merchant_store_list = [axe, backpack_object, helmet]
        fall_scene_merchant = Merchant(merchant_store_list)
        fall_scene_merchant.merchant_dialogue(traveler)

        print(f"\nMain character's backpack: {traveler.backpack.backpack_storage}")
        print(f"Main character's coin storage: {traveler.coin_storage} coins\n")

    def travel_function(self, traveler):
        # Create the all the locations -> Farm, forrest, great pumpkin
        farm = Farm("Farm")
        great_pumpkin = Great_Pumpkin("Great_Pumpkin")
        forest = Forest("Forest", great_pumpkin)

        # Both the farm and the forest need to be discovered to move on to have the option to go to the great pumpkin
        while not farm.discovered and not forest.discovered:
            print("Where would you like to travel to? Enter the number corresponding to the place.\n\n")
            print("[0]Farm\n")
            print("[1]Forest\n")
            travel_action = input()
            if travel_action == "0":
                farm.location_scene(traveler)
                farm.discovered = True
            elif travel_action == "1":
                forest.location_scene(traveler)
                forest.discovered = True
            else:
                print("Please enter a number that corresponds to a place")

        while not great_pumpkin.completed:
            print("Where would you like to travel to? Enter the number corresponding to the place.\n\n")
            print("[0]Farm\n")
            print("[1]Forest\n")
            print("[2]Great Pumpkin\n")
            travel_action = input()
            if travel_action == "0":
                farm.location_scene(traveler)
                farm.discovered = True
            elif travel_action == "1":
                forest.location_scene(traveler)
                forest.discovered = True
            elif travel_action == "2":
                great_pumpkin.location_scene(traveler)
            else:
                print("Please enter a number that corresponds to a place")
