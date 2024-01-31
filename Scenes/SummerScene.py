
from User_Objects.Armor import Armor
from User_Objects.Key import Key
from User_Objects.Weapon import Weapon
from User_Objects.Backpack import Backpack

from Characters.Main_Character import MainCharacter
from Characters.Merchant_Character import Merchant

class summer_scene:
    #toggle vars
    first_plains_visit = True
    first_barn_visit = True
    first_cave_visit = True
    knight_is_alive = True
    entrance_first_visit = True

    # Initiates the opening of the Summer scene
    def run_scene(traveler: MainCharacter, first_visit):
        if first_visit:
            print("You get to the end of the viney clearing, finding yourself at the top of a steep hillside. You're enveloped by what feels like a wall of heat as you walk forward. This is the final realm. The final season before you reach Timebro. Summer.\n")
            print("You can see Timebro's tower straight ahead, to the far North. You just need to get to him and this will all be over.")
            summer_scene.entrance_first_visit = False
            
        else:
            print("You overlook the reach once more.")
        summer_scene.intro_choices()

    def intro_choices():
        zones = ["1","2","3"]
        destination = ""
        print("You see plains straight ahead, between you and the tower. You'll have to cross them to get to Timebro. To the East you see a gaping cave mouth. The insides are a mystery. To the far west, you can see an abandoned barn. Perhaps it can be looted.\n")
        while destination not in zones:
            print("Where do you go?\n\nOPTIONS:\n1 - plains\n2 - cave\n3 - barn")
            destination = input()
            if destination is "1":
                summer_scene.plains(summer_scene.first_plains_visit, summer_scene.knight_is_alive)
            elif destination is "2":
                summer_scene.cave(summer_scene.first_cave_visit)
            elif destination is "3":
                summer_scene.barn(summer_scene.first_barn_visit)

            

    def plains(first_visit, knight_alive):
        if first_visit and knight_alive:
            print("You walk across the lengthy field and notice a figure approaching in the distance. As you get closer, you realize he's much larger than you first thought. A hulking titan wearing a menacing suit of armor. He lodges his greatsword in the ground and speaks: '" +MainCharacter.__name__+ "!', he exclaims, 'I cannot let you go any further.'\n")
            summer_scene.first_visit = False
            summer_scene.plains_event_1()

        elif knight_alive:
            print("The knight jeers at you and speaks: 'Returning once more after your cowardly retreat? What do you want?'")
            summer_scene.plains_event_1()
        else:
            print("With the Titanic Knight dead, the way to the tower is now clear.\n")
            summer_scene.plains_event_2()

    def plains_event_1():
            plains_choice = ""
            plains_options = ["1","2"]
            while plains_choice not in plains_options:
                print("What do you do?\n\nOPTIONS:\n1 - fight\n2 - run")
                plains_choice = input()
                if plains_choice is "1":
                    #Program Combat Mechanics
                    done = False
                elif plains_choice is "2":
                    print("You run back to the hillside, with your tail between your legs.")
                    summer_scene.intro_choices()

    def plains_event_2():
            plains_choice = ""
            plains_options = ["1","2"]
            while plains_choice not in plains_options:
                print("Do you proceed?\n\nOPTIONS:\n1 - Yes\n2 - No")
                plains_choice = input()
                if plains_choice is "1":
                    print("You march on, ready for whatever may come next.")
                    #tower():
                elif plains_choice is "2":
                    print("You turn back, not yet ready to face Timebro.")
                    summer_scene.intro_choices()

    def cave(first_visit):
        if first_visit:
            print("You arrive at the cave, and the first thing you notice is that it's strikingly dark, almost darker than it should be. You're certain you won't be able to navigate without a light. There are several old barrels lying around the outside, though they look to be filled with dirt and other refuse.")
            summer_scene.cave_event_1()
        else:
            print("You return to the cave, curious what else it may be hiding.")
            summer_scene.cave_event_1()    
    
    def cave_event_1():
        cave_choice = ""
        cave_options = ["1","2","3"]

        while cave_choice not in cave_options:
            print("What do you do?\n\nOPTIONS:\n1 - Explore Cave\n2 - Rummage Through Barrels")
            cave_choice = input()
            if cave_choice is "1":
                has_lantern = False
                #CHECK IF THEY HAVE LANTERN??
                if has_lantern is False:
                    print("Against your better judgement, you walk into the cave without a light to shine the way. You walk until you can't see anything around you, until eventually you hear growling. You don't even have time to react before the source of the sound eats you in one bite.\n\n YOU HAVE DIED")
                elif has_lantern is True:
                    summer_scene.cave_event_2()
            elif cave_choice is "2":
                #ADD ITEM TO LOOT
                print("You rummage for loot in the barrels, and most of them hold nothing of note. A glint catches your eye in one of them though, and you reach in to dig around for whatever it was. You feel something solid, and you pull your hand out to reveal a silver ring, with a purple gemstone encrested in it.")


    def cave_event_2():
        print("You press into the cave with your trusty Everflame lantern, and as you walk deeper through the tunnels, you hear something whimper away from the light, retreating further into the darkness of the cave. The tunnel eventually opens into a circular space with another tunnel on the other side. The tunnel has a different texture to it, almost flesh-like rather than stone. In the middle of this room is a sword in a stone.")
        summer_scene.cave_event_3()

    def cave_event_3():
        cave_choice_2 = ""
        cave_options_2 = ["1","2","3"]
        while cave_choice_2 not in cave_options_2:
            print("What do you do?\n\nOPTIONS:\n1 - Pull The Sword Out\n2 - Press Deeper\n3 - Turn Around")
            cave_choice_2 = input()
            if cave_choice_2 is "1":
                #ADD SWORD TO WEAPONS
                print("The sword pulls from the stone with relative ease; you heft it in your hands, and it feels... right. You're unsure how, but you know the name of this sword: Rexcalibur.")
            elif cave_choice_2 is "2":
                print("You take one step down the next tunnel, and gaping jaws clamp down on you. It wasn't a tunnel at all!\n\nYOU HAVE DIED")
            elif cave_choice_2 is "3":
                print("You turn around, and return to the entrance of the cave.")
                summer_scene.cave()

    def barn(first_visit):
        if first_visit:
            print("You arrive at the barn, and it looks more worn down up close. Despite this, it appears to be the only standing structure aside from the tower for miles. Miscellaneous supplies are strewn about outside, and the front door doesn't appear to be locked.")
            summer_scene.barn_event_1()
        else:
            print("You arrive at the barn once more. You wonder if it looks even more worn down since you were here last.")
            summer_scene.barn_event_1()

    def barn_event_1():
        barn_choice = ""
        barn_options = ["1","2","3"]
        while barn_choice not in barn_options:
            print("What do you do?\n\nOPTIONS:\n1 - Pull on Front Door\n2 - Knock on Front Door\n3 - Search Through Supplies")
            barn_choice = input()
            if barn_choice is "1":
                print("You give the handle a pull, but it doesn't budge. Perhaps the door is barred from the inside.")
                #tower():
            elif barn_choice is "2":
                print("You knock on the door, and after a long pause you eventually hear 'Who's there?!'. They sound irritated and anxious.")
                summer_scene.intro_choices()
            elif barn_choice is "3":
                done = False

    def barn_event_2():
        barn_choice = ""
        barn_options = ["1","2"]
        while barn_choice not in barn_options:
            print("What do you say?\n\nOPTIONS:\n1 - "+MainCharacter.name+"\n2 - Timebro")
            barn_choice = input()
            if barn_choice is "1":
                print("There's another pause. 'Haven't heard that name before. You must be another survivor. Here, let me get the door for ya.' You hear a sliding sound, and then the door opens to reveal a man in ragged clothing. He gestures inside.")

            elif barn_choice is "2":
                print("Another pause, then you hear a scoff through the door. 'So that's what you're calling yourself now? Don't make yourself out to be a bigger fool than you already are, Johnny. Go away.' You step back and take in your surroundings again.")
                summer_scene.barn_event_1()
    def barn_event_3():
        barn_choice = ""
        barn_options = ["1","2"]
        while barn_choice not in barn_options:
            print("What do you do?\n\nOPTIONS:\n1 - Enter the Barn\n2 - Back Away")
            barn_choice = input()
            if barn_choice is "1":
                print("You walk inside, and see only darkness until your eyes adjust to the dim light of the oil lamp hanging from a wood beam. Once you can see again, you realize there's several other people scattered around the barn. Presumably other survivors.")
                print("\n'These are all the people left in this area. The rest didn't make it when Johnny cast that heat wave.")
            elif barn_choice is "2":
                print("'Suit yourself,' the man says, closing the door once more.")
                summer_scene.barn_event_1()

    def barn_event_4():
        done = False

    run_scene(MainCharacter,entrance_first_visit)