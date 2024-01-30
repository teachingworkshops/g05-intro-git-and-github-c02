
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
        summer_scene.intro_choices()

    def intro_choices():
        zones = ["plains,cave,barn,tower,lakebed"]
        print("You see plains straight ahead, between you and the tower. You'll have to cross them to get to Timebro.\n")
        print("To the East you see a gaping cave mouth. The insides are a mystery.\n")
        print("To the far west, you can see an abandoned barn. Perhaps it can be looted.\n")
        print("Where do you go? OPTIONS: plains/cave/barn")
    run_scene(MainCharacter)