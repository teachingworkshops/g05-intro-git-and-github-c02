
from User_Objects.Armor import Armor
from User_Objects.Key import Key
from User_Objects.Weapon import Weapon
from User_Objects.Backpack import Backpack

from Characters.Main_Character import MainCharacter
from Characters.Merchant_Character import Merchant

class summer_scene():


    # Initiates the opening of the Summer scene
    def run_scene(traveler: MainCharacter):
        print("You get to the end of the viney clearing, finding yourself at the top of a steep hillside.\n")
        print("You're struck with a wall of heat as you walk forward. This is the final season.\n")
        print("The final realm before you reach Timebro. Summer.\n")

    def intro_choices():
        zones = ["plains,cave,barn,tower,lakebed"]
        print("Where do you go?")
    run_scene(MainCharacter)