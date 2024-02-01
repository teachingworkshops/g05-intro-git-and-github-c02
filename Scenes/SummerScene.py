
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
    first_tower_visit = True
    first_entrance_visit = True
    knight_is_alive = True
    player_has_ring = False
    player_has_rexcalibur = False
    lied_at_barn = False
    timebro_secret = False

    # Initiates the opening of the Summer scene
    def run_scene(traveler: MainCharacter):
        if summer_scene.first_entrance_visit:
            print("You get to the end of the viney clearing, finding yourself at the top of a steep hillside. You're enveloped by what feels like a wall of heat as you walk forward. This is the final realm. The final season before you reach Timebro. Summer.\n")
            print("You can see Timebro's tower straight ahead, to the far North. You just need to get to him and this will all be over.")
            print("You see plains straight ahead, between you and the tower. You'll have to cross them to get to Timebro. To the East you see a gaping cave mouth. The insides are a mystery. To the far west, you can see an abandoned barn. Perhaps it can be looted.\n")

            summer_scene.entrance_first_visit = False
            
        else:
            print("You overlook the lands once more.")
        summer_scene.intro_choices()

    def intro_choices():
        zones = ["1","2","3"]
        destination = ""
        while destination not in zones:
            print("Where do you go?\n\nOPTIONS:\n1 - plains\n2 - cave\n3 - barn")
            destination = input()
            if destination == "1":
                summer_scene.plains(summer_scene.first_plains_visit, summer_scene.knight_is_alive)
            elif destination == "2":
                summer_scene.cave(summer_scene.first_cave_visit)
            elif destination == "3":
                summer_scene.barn(summer_scene.first_barn_visit)

            

    def plains(first_visit, knight_alive):
        if first_visit and knight_alive:
            print("You walk across the lengthy field and notice a figure approaching in the distance. As you get closer, you realize he's much larger than you first thought. A hulking titan wearing a menacing suit of armor. He lodges his greatsword in the ground and speaks: '" +MainCharacter.__name__+ "!', he exclaims, 'I cannot let you go any further.'\n")
            summer_scene.first_visit = False
            summer_scene.plains_event_1(summer_scene.player_has_rexcalibur)

        elif knight_alive:
            print("The knight jeers at you and speaks: 'Returning once more after your cowardly retreat? What do you want?'")
            summer_scene.plains_event_1(summer_scene.player_has_rexcalibur)
        else:
            print("With the Titan Knight dead, the way to the tower is now clear.\n")
            summer_scene.plains_event_2()

    def plains_event_1(has_rexcalibur):
            plains_choice = ""
            plains_options = ["1","2"]
            while plains_choice not in plains_options:
                print("What do you do?\n\nOPTIONS:\n1 - fight\n2 - run")
                plains_choice = input()
                if plains_choice == "1":
                    if has_rexcalibur:
                        print("Using Rexcalibur, you fell the knight in a single swing.")
                        summer_scene.knight_is_alive = False
                        summer_scene.plains(summer_scene.first_plains_visit)
                    if not has_rexcalibur:
                        print("You try to go in for a swing, but the knight is too fast, and too strong. He swipes at you and cuts you clean in half.\n\nYOU HAVE DIED.")

                elif plains_choice == "2":
                    print("You run back to the hillside, with your tail between your legs.")
                    summer_scene.intro_choices()

    def plains_event_2():
            plains_choice = ""
            plains_options = ["1","2"]
            while plains_choice not in plains_options:
                print("Do you proceed?\n\nOPTIONS:\n1 - Yes\n2 - No")
                plains_choice = input()
                if plains_choice == "1":
                    print("You march on, ready for whatever may come next.")
                    summer_scene.tower(summer_scene.first_tower_visit)
                elif plains_choice == "2":
                    print("You turn back, not yet ready to face Timebro.")
                    summer_scene.intro_choices()

    def cave(first_visit):
        if first_visit:
            print("You arrive at the cave, and the first thing you notice is that it's strikingly dark, almost darker than it should be. You're certain you won't be able to navigate without a light. There are several old barrels lying around the outside, though they look to be filled with dirt and other refuse.")
            summer_scene.cave_event_1()
            summer_scene.first_cave_visit = False
        else:
            print("You return to the cave entrance, curious what else it may be hiding.")
            summer_scene.cave_event_1()    
    
    def cave_event_1():
        cave_choice = ""
        cave_options = ["1","2","m"]

        while cave_choice not in cave_options:
            print("What do you do?\n\nOPTIONS:\n1 - Explore Cave\n2 - Rummage Through Barrels\nm - map")
            cave_choice = input()
            if cave_choice == "1":
                has_lantern = False
                #CHECK IF THEY HAVE LANTERN??
                if has_lantern == False:
                    print("Against your better judgement, you walk into the cave without a light to shine the way. You walk until you can't see anything around you, until eventually you hear growling. You don't even have time to react before the source of the sound eats you in one bite.\n\n YOU HAVE DIED")
                elif has_lantern == True:
                    summer_scene.cave_event_2()
            elif cave_choice == "2":
                #ADD ITEM TO LOOT
                print("You rummage for loot in the barrels, and most of them hold nothing of note. A glint catches your eye in one of them though, and you reach in to dig around for whatever it was. You feel something solid, and you pull your hand out to reveal a silver ring, with a purple gemstone encrested in it.")
                summer_scene.cave(summer_scene.first_cave_visit)
            elif cave_choice == "m":
                summer_scene.cave_map()

    def cave_event_2():
        print("You press into the cave with your trusty Everflame lantern, and as you walk deeper through the tunnels, you hear something whimper away from the light, retreating further into the darkness of the cave. The tunnel eventually opens into a circular space with another tunnel on the other side. The tunnel has a different texture to it, almost flesh-like rather than stone. In the middle of this room is a sword in a stone.")
        summer_scene.cave_event_3()

    def cave_event_3():
        cave_choice_2 = ""
        cave_options_2 = ["1","2","3"]
        while cave_choice_2 not in cave_options_2:
            print("What do you do?\n\nOPTIONS:\n1 - Pull The Sword Out\n2 - Press Deeper\n3 - Turn Around")
            cave_choice_2 = input()
            if cave_choice_2 == "1":
                #ADD SWORD TO WEAPONS
                print("The sword pulls from the stone with relative ease; you heft it in your hands, and it feels... right. You're unsure how, but you know the name of this sword: Rexcalibur.")
            elif cave_choice_2 == "2":
                print("You take one step down the next tunnel, and gaping jaws clamp down on you. It wasn't a tunnel at all!\n\nYOU HAVE DIED")
            elif cave_choice_2 == "3":
                print("You turn around, and return to the entrance of the cave.")
                summer_scene.cave(summer_scene.first_cave_visit)

    def barn(first_visit):
        if first_visit:
            print("You arrive at the barn, and it looks more worn down up close. Despite this, it appears to be the only standing structure aside from the tower for miles. Miscellaneous supplies are strewn about outside, and the front door doesn't appear to be locked.")
        else:
            print("You arrive at the barn once more. You wonder if it looks even more worn down since you were here last.")
        summer_scene.barn_event_1(summer_scene.lied_at_barn)

    def barn_event_1(lied):
        barn_choice = ""
        barn_options = ["1","2","3","m"]
        while barn_choice not in barn_options:
            print("What do you do?\n\nOPTIONS:\n1 - Pull on Front Door\n2 - Knock on Front Door\n3 - Search Through Supplies\nm - map")
            barn_choice = input()
            if barn_choice == "1":
                print("You give the handle a pull, but it doesn't budge. Perhaps the door is barred from the inside.")
                summer_scene.barn_event_1(summer_scene.lied_at_barn)
            elif barn_choice == "2":
                if lied:
                    print("You hear a voice inside again: 'Leave us alone, Johnny. You've already doomed us.'")
                    summer_scene.barn_event_1()
                else:
                    print("You knock on the door, and after a long pause you eventually hear 'Who's there?!'. They sound irritated and anxious.")
                    summer_scene.barn_event_2()
            elif barn_choice == "3":
                print("you rummage through the supplies, but find nothing of note.")
                summer_scene.barn_event_1()
            elif barn_choice == "m":
                summer_scene.barn_map()

    def barn_event_2():
        barn_choice = ""
        barn_options = ["1","2"]
        while barn_choice not in barn_options:
            print("What do you say?\n\nOPTIONS:\n1 - "+MainCharacter.name+"\n2 - Timebro")
            barn_choice = input()
            if barn_choice == "1":
                print("There's another pause. 'Haven't heard that name before. You must be another survivor. Here, let me get the door for ya.' You hear a sliding sound, and then the door opens to reveal a man in ragged clothing. He gestures inside.")
                summer_scene.barn_event_3()

            elif barn_choice == "2":
                print("Another pause, then you hear a scoff through the door. 'So that's what you're calling yourself now? Don't make yourself out to be a bigger fool than you already are, Johnny. Go away.' You step back and take in your surroundings again.")
                summer_scene.barn_event_1()
                
    def barn_event_3():
        barn_choice = ""
        barn_options = ["1","2"]
        while barn_choice not in barn_options:
            print("What do you do?\n\nOPTIONS:\n1 - Enter the Barn\n2 - Back Away")
            barn_choice = input()
            if barn_choice == "1":
                print("You walk inside, and see only darkness until your eyes adjust to the dim light of the oil lamp hanging from a wood beam. Once you can see again, you realize there's several other people scattered around the barn. Presumably other survivors.")
                print("\n'Didn't think there were any others out there. My name is Yomen. These folks are all the people left in this area. The rest didn't make it when Johnny cast that heat wave.")
                summer_scene.barn_event_4()
            elif barn_choice == "2":
                print("'Suit yourself,' the man says, closing the door once more.")
                summer_scene.barn_event_1()

    def barn_event_4():
        barn_choice = ""
        barn_options = ["1","2"]
        while barn_choice not in barn_options:
            print("What do you say?\n\nOPTIONS:\n1 - Who's Johnny?\n2 - How long have you all been here?")
            plains_choice = input()
            if plains_choice == "1":
                print("'Who's Johnny?! He's the one who caused this whole mess! Meddled with the arcane for some time, but lost the ring that kept his magic contained. Went crazy after that.'")
                summer_scene.barn_event_5()
            elif plains_choice == "2":
                print("'We've been here for months, hiding out from the heat and scavenging for survival. You can lay low with us if you like, but you'll have to help gather resources.'")
                summer_scene.intro_choices()

    def barn_event_5():
        barn_choice = ""
        barn_options = ["1","2"]
        while barn_choice not in barn_options:
            print("What do you do?\n\nOPTIONS:\n1 - Tell Yomen you've come to defeat Timebro\n2 - Leave")
            plains_choice = input()
            if plains_choice == "1":
                print("Yomen snorts. 'So that's what they're calling him now? Well, on the off chance you do come face to face with him, speak the words 'Adnus Incanum'. It will temporary weaken the magic's hold on him. Now if you're not going to help us scavenge, you'd best get going.")
                summer_scene.timebro_secret = True
            elif plains_choice == "2":
                print("Good luck out there.")
            print("You return to the entrance of the barn.")
            summer_scene.barn_event_1()

    def barn_event_6():
        barn_choice = ""
        barn_options = ["1","2"]
        while barn_choice not in barn_options:
            print("Do you stay with the survivors?\n\nOPTIONS:\n1 - Yes\n2 - No")
            plains_choice = input()
            if plains_choice == "1":
                print("You give up on your quest early, instead offering aid to the survivors in the barn. Together you scrap together what you can to survive, but ultimately you can't outlast the calamity of timebro.\n\nYOU HAVE DIED.")
            elif plains_choice == "2":
                print("'Suit yourself. Our door's always open if you come back. Well, not literally, but you get it.'")
                print("You return to the entrance of the barn.")
                summer_scene.barn_event_1()

    def tower(first_visit):
        if first_visit:
            print("You arrive at the base of the tower, only to see the door is sealed shut, and not with any lock. It has arcane scripture scrawled in glowing text across it.\n")
            print("The inscription looks like it was written by a madman, readying only 'FIND THE RING FIND THE RING FIND THE RING', repeating from top to bottom. There is a ring-shaped slot in the center.")
            summer_scene.first_tower_visit = False
            summer_scene.tower_event_1()
        else:
            print("The tower stands before you, menacingly.")
            summer_scene.tower_event_1()

    def tower_event_1():
        tower_choice = ""
        tower_options = ["1","2","3"]
        while tower_choice not in tower_options:
            if summer_scene.player_has_ring:
                print("What do you do?\n\nOPTIONS:\n1 - Touch the door\n2 - Walk away\n3 - Insert ring into the slot")
            else:
                print("What do you do?\n\nOPTIONS:\n1 - Touch the door\n2 - Walk away")   
            map_choice = input()
            if map_choice == "1":
                print("You reach for the door, but as soon as a finger touches it you're zapped with arcane energy.")
                summer_scene.tower_event_1()
            elif map_choice == "2":
                summer_scene.tower(summer_scene.first_tower_visit)
            elif map_choice == "3":
                print("You place the ring into the slot, and it's a perfect fit. The door rumbles and slides open, dropping the ring on the ground. You pick it back up.")    
                summer_scene.tower_event_2()

    def tower_event_2():
        tower_choice = ""
        tower_options = ["1","2"]
        while tower_choice not in tower_options:
            print("Do you enter the tower?\n\nOPTIONS:\n1 - Yes\n2 - No")
            tower_choice = input()
            if tower_choice == "1":
                print("You walk in, ready to confront Timebro.")
                summer_scene.tower_event_3()
            elif tower_choice == "2":
                print("You turn around. Timebro can wait.")
                summer_scene.tower(summer_scene.first_tower_visit)

    def tower_event_3():
        print("You walk inside the tower, and Timebro stands before you, looming over you at a menacing 5 feet even. His eyes look frantic. 'DO YOU HAVE THE RING?'")
        summer_scene.tower_event_4()

    def tower_event_4():
        tower_choice = ""
        tower_options = ["1","2","3"]
        while tower_choice not in tower_options:
            if summer_scene.timebro_secret:
                print("What do you tell Timebro?\n\nOPTIONS:\n1 - Yes\n2 - No\n3 - Adnus Incanum")
            else:
                print("What do you tell Timebro?\n\nOPTIONS:\n1 - Yes\n2 - No")
            tower_choice = input()
            if tower_choice == "1":
                print("'FINALLY!' He snatches the ring from you and slides it on his finger. What appears to be relief on his face quickly shifts to pain as the ring absorbs all the excess magic from him. He tries to rip the ring off, but it's too late. All the magic is absorbed from him, and he collapses to the floor.\n\n YOU WIN?")
                summer_scene.tower_event_3()
            elif tower_choice == "2":
                print("'THEN PERISH,' he bellows, as he blasts you with a magic beam of death.\n\nYOU HAVE DIED.")
                summer_scene.tower(summer_scene.first_tower_visit)
            elif tower_choice == "3" and summer_scene.timebro_secret:
                print("He looks at you strangely, but then the incantation takes effect. He gasps for breath before speaking 'It's too late for me, traveler. I'm already one with this power. I have no ability to stop it myself, but that ring can. Let me end this.' He gets these words out before falling back into his frantic state. 'WELL? DO YOU HAVE THE RING?'")
                summer_scene.tower_event_4()

    def barn_map():
        map_choice = ""
        map_options = ["1","2","3"]
        while map_choice not in map_options:
            print("Where will you travel?\n\nOPTIONS:\n1 - Hillside\n2 - Plains\n3 - Cave")
            map_choice = input()
            if map_choice == "1":
                summer_scene.intro_choices()
            elif map_choice == "2":
                summer_scene.plains(summer_scene.first_plains_visit)
            elif map_choice == "3":
                summer_scene.cave(summer_scene.first_cave_visit)

    def cave_map():
        map_choice = ""
        map_options = ["1","2","3"]
        while map_choice not in map_options:
            print("Where will you travel?\n\nOPTIONS:\n1 - Hillside\n2 - Plains\n3 - Barn")
            map_choice = input()
            if map_choice == "1":
                summer_scene.intro_choices()
            elif map_choice == "2":
                summer_scene.plains(summer_scene.first_plains_visit)
            elif map_choice == "3":
                summer_scene.barn(summer_scene.first_barn_visit)
    def tower_map():
        map_choice = ""
        map_options = ["1","2","3"]
        while map_choice not in map_options:
            print("Where will you travel?\n\nOPTIONS:\n1 - Barn\n2 - Plains\n3 - Cave")
            map_choice = input()
            if map_choice == "1":
                summer_scene.barn(summer_scene.first_barn_visit)
            elif map_choice == "2":
                summer_scene.plains(summer_scene.first_plains_visit)
            elif map_choice == "3":
                summer_scene.cave(summer_scene.first_cave_visit)
