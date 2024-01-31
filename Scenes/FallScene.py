# Fall scene for the story

from User_Objects.Armor import Armor
from User_Objects.Key import Key
#from User_Objects.Item import item
from User_Objects.Weapon import Weapon
from User_Objects.Backpack import Backpack

from Characters.Main_Character import MainCharacter
from Characters.Merchant_Character import Merchant

class fall_scene:
    def __init__(self):
        self.locations = []
    # Runs the fall scene
    def run_scene(traveler: MainCharacter):
        print("Welcome to the Fall Scene!\n")
        print("To begin there will be a traveling merchant at the start of each scene. Would you like to speak with the merchant?\n")
        while True: 
            talk_to_merchant = input("Enter ['y'] for yes or ['n'] for no\n")
            if talk_to_merchant == 'y':
                fall_scene.merchant_scene(traveler)
                break # Ends while loop
            elif talk_to_merchant == 'n':
                break # Ends while loop
            else:
                print("Please answer with 'y' or 'n.\n")

        print("Where would you like to explore?\n")
        input("[0]")

    # Tests the merchants dialogue and function of buying from the merchant 
    def merchant_scene(traveler):
        # Creates items for the character to buy
        axe = Weapon("Battle Axe", "A weapon that deals damage to enemies.", True, 25, 35)
        backpack_object = Backpack("Backpack", "Carries items that you pick up", True, 50, 5)
        helmet = Armor("Helmet", "Adds protection to any danger that approaches", True, 35, "head", 50)

        merchant_store_list = [axe, backpack_object, helmet]
        fall_scene_merchant = Merchant(merchant_store_list)
        fall_scene_merchant.merchant_dialogue(traveler)

        print(f"\nMain character's backpack: {traveler.backpack.backpack_storage}")
        print(f"Main character's coin storage: {traveler.coin_storage} coins\n")

    def travel_function():
        print("Where would you like to travel to? Enter the number corresponding to the place.\n\n")
        print("[0]Farm\n")
        print("[1]Forest\n")
        travel_action = input()
        if travel_action == "0":
            print("")
            # Farm location
        elif travel_action == "1":
            print("")
            # Forest location
        else:
            print("Please enter a number that corresponds to a place")

# -- Farm Location -- 
        
        # Need to create Farm location
        # Farm location has sublocations: Barn, horse stables, once those have been discovered add corn maze

        # Create a farmer character
        
    # -- Barn Sub-Location -- 
        
    # -- Horse Stable Sub-Location --
        
    # -- Corn Maze Sub-Location --
        
# -- Forest Location -- 
        
# -- Pumpkin Location (Final Location) --
        


        
