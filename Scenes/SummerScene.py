
from User_Objects.Armor import Armor
from User_Objects.Key import Key
from User_Objects.Weapon import Weapon
from User_Objects.Backpack import Backpack

from Characters.Main_Character import MainCharacter
from Characters.Merchant_Character import Merchant

class summer_scene:
    #plains vars
    first_plains_visit = True
    first_barn_visit = True
    first_cave_visit = True
    knight_is_alive = True

    # Initiates the opening of the Summer scene
    def run_scene(traveler: MainCharacter):
        print("You get to the end of the viney clearing, finding yourself at the top of a steep hillside. You're enveloped by what feels like a wall of heat as you walk forward. This is the final realm. The final season before you reach Timebro. Summer.\n")
        print("You can see Timebro's tower straight ahead, to the far North. You just need to get to him and this will all be over.")
        
        summer_scene.intro_choices()

    def intro_choices():
        zones = ["1","2","3"]
        destination = ""
        print("You see plains straight ahead, between you and the tower. You'll have to cross them to get to Timebro. To the East you see a gaping cave mouth. The insides are a mystery. To the far west, you can see an abandoned barn. Perhaps it can be looted.\n")
        while destination not in zones:
            print("Where do you go?\nOPTIONS:\n1 - plains\n2 - cave\n3 - barn")
            destination = input()
            if destination is "1":
                summer_scene.plains(summer_scene.first_plains_visit, summer_scene.knight_is_alive)
            elif destination is "2":
                summer_scene.cave(summer_scene.first_cave_visit)
            elif destination is "3":
                summer_scene.barn
            else:
                print("Enter a valid option. \n")
            

    def plains(first_visit, knight_alive):
        if first_visit:
            print("You walk across the lengthy field and notice a figure approaching in the distance. As you get closer, you realize he's much larger than you first thought. A hulking titan wearing a menacing suit of armor. He lodges his greatsword in the ground and speaks: '" +MainCharacter.__name__+ "!', he exclaims, 'I cannot let you go any further.'\n")

            plains_choice = ""
            plains_options = ["1","2"]
            while plains_choice not in plains_options:
                print("What do you do?\nOPTIONS:\n1 - fight\n2 - run")
                plains_choice = input()
                if plains_choice is "1":
                    done = False
                elif plains_choice is "2":
                    done = False

    def cave(first_visit):
        print("You arrive at the cave, and the first thing you notice is that it's strikingly dark, almost darker than it should be. You're certain you won't be able to navigate without a light. There are several old barrels lying around the outside. You could look them over for anything useful")
        cave_choice = ""
        cave_options = ["1","2","3"]

        while cave_choice not in cave_options:
            print("What do you do?\nOPTIONS:\n1 - Explore Cave\n2 - Rummage Through Barrels")
            plains_choice = input()
            if plains_choice is "1":
                done = False
            elif plains_choice is "2":
                done = False
    def barn(first_visit):
        done = False
    run_scene(MainCharacter)