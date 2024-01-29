# Fall scene for the story

from User_Objects.Armor import Armor
from User_Objects.Key import Key
#from User_Objects.Item import item
from User_Objects.Weapon import Weapon
from User_Objects.Backpack import Backpack

from Characters.Main_Character import MainCharacter
from Characters.Merchant_Character import Merchant

class fall_scene:
    # Runs the fall scene
    def run_scene(traveler: MainCharacter):
        print("Welcome to the Fall Scene!\n")
        fall_scene.merchant_test(traveler)

    # Tests the merchants dialogue and function of buying from the merchant 
    def merchant_test(traveler):
        print("---- Merchant Test: ----\n\n")
        print(f"Traveler begins with {traveler.coin_storage} coins\n")
        print("Creating three items: a sword, a backpack, a helmet\n\n\n")
        sword = Weapon("sword", "a weapon that deals damage to enemies", 25, 50)
        backpack_object = Backpack("backpack", "carries items that you pick up", 50, 5)
        helmet = Armor("helmet", "adds protection to any danger that approaches", 35, "head", 50)

        merchant_store_list = [sword, backpack_object, helmet]
        fall_scene_merchant = Merchant(merchant_store_list)
        fall_scene_merchant.merchant_dialogue(traveler)

        print(f"\nMain character's backpack: {traveler.backpack.backpack_storage}")
        print(f"Main character's coin storage: {traveler.coin_storage} coins\n")

# -- Farm Location -- 
        
        # Need to create Farm location
        # Farm location has sublocations: Barn, horse stables, once those have been discovered add corn maze

        # Create a farmer character
        
    # -- Barn Sub-Location -- 
        
    # -- Horse Stable Sub-Location --
        
    # -- Corn Maze Sub-Location --
        
# -- Forest Location -- 
        
# -- Pumpkin Location (Final Location) --
        


        
