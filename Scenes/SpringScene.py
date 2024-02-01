from User_Objects.Armor import Armor
from User_Objects.Key import Key
from User_Objects.Weapon import Weapon
from User_Objects.Backpack import Backpack

from Characters.Main_Character import MainCharacter
from Characters.Merchant_Character import Merchant

class spring_scene():
    first_part = False
    second_part = False
    third_part = False
    end = False

    def has_all_spells(first, second, third):
        return first and second and third

    def run_scene(traveler:MainCharacter):
        print("As you leave the freezing winter, you enter the warm embrace of Spring. Following a path through a field,")
        print("you realize that this is area is no normal area.\nThe whole area is filled with enchantment and magic.")
        print("Who knows what you will encounter. You continue following the path through the field until you encounter")
        print("a giant, thick wall of vines blocking your path. How will you get through?")
        spring_scene.field_scene()

    def field_scene():
        while True:
            if (spring_scene.has_all_spells(spring_scene.first_part, spring_scene.second_part, spring_scene.third_part)):
                print("What would you like to do?\nInvestigate(i), Travel(t), Cast Spell(c)")
            else:
                print("What would you like to do?\nInvestigate(i), Travel(t)")
            action = input()
            print()

            if action == 'i':
                print("There seems to be a sign with some sort of inscription:")
                print("The great wall of vines will fall, when the spell is spoken.")
                print("It looks like the rest of the sign is broken off. Perhaps the missing pieces are somewhere around.")
            elif action == 't':
                break
            elif spring_scene.has_all_spells and action == 'c':
                spring_scene.end = True
                print("Great wall of vines, bind no more,\nUnravel now, from base to spore.\nWith whispered winds and sunlight's grace,\nUntangle, uncoil, reveal the space")
                break
            else:
                print("This action is not known.")

        if spring_scene.end:
            spring_scene.ending_scene()
        else:
            while True:
                print("Where would you like to go?\nOPTIONS: Calming River(r), Enchanted Forest(f), Flower Garden(g)")
                dest = input()
                print()

                if dest == 'r':
                    spring_scene.river_scene()
                    break
                elif dest == 'f':
                    spring_scene.forest_scene()
                    break
                elif dest == 'g':
                    spring_scene.garden_scene()
                    break
                else:
                    print('This place is not known.')
    
    investigated_river = False

    def river_scene():
        print("The calming river is very peaceful, yet the river is filled with life.")

        while True:
            if spring_scene.investigated_river:
                print("What would you like to do?\nInvestigate(i), Travel(t), Go in Water(w)")
            else:
                print("What would you like to do?\nInvestigate(i), Travel(t)")
            
            action = input()
            print()

            if action == 'i':
                if not spring_scene.first_part:
                    spring_scene.investigated_river = True
                    print("Something has caught your eye at the bottom of the river. It looks like a broken piece of wood.")
                else:
                    print("There is nothing new.")
            elif action == 't':
                break
            elif spring_scene.investigated_river and action == 'w':
                if not spring_scene.first_part:
                    spring_scene.first_part = True
                    print("You pick up the piece of wood in the water, but it's perfectly dry. It looks like the first piece")
                    print("of the missing spell!")
                else:
                    print("There is nothing else in the water.")
            else:
                print("This action is not known.")

        if spring_scene.end:
            spring_scene.ending_scene()
        else:
            while True:
                print("Where would you like to go?\nOPTIONS: Magical Fields(f)")
                dest = input()
                print()

                if dest == 'f':
                    spring_scene.field_scene()
                    break
                else:
                    print('This place is not known.')

    investigated_forest = False
    found_key = False
    count = 0

    def print_forest(count):
        if count == 0:
            print("What? You swear you just came from here. Why does it look exactly the same?")
        elif count == 1:
            print("Are you walking in circles? This can't be...")
        elif count == 2:
            print("It's the same place! But what is that glowing light?")
        else:
            print("Hmm... maybe I should investigate.")

    def forest_scene():
        if spring_scene.count == 0:
            print("enchanted forest")

        while True:
            if spring_scene.investigated_forest:
                print("What would you like to do?\nInvestigate(i), Travel(t), Go towards Light(l)")
            else:
                print("What would you like to do?\nInvestigate(i), Travel(t)")
            
            action = input()
            print()

            if action == 'i':
                if spring_scene.count >= 3:
                    spring_scene.investigated_forest = True
                    print("you found a shiny light")
                else:
                    print("there seems to be nothing around. looks like i can keep going.")
            elif action == 't':
                break
            elif spring_scene.count >= 3 and action == 'l':
                if not spring_scene.found_key:
                    spring_scene.found_key = True
                    print("you found a key")
                else:
                    print("nothing else in the light")
            else:
                print("action not known")

        while True:
            print("where would you like to go?\nOPTIONS: Deeper into the Enchanted Forest(e), Abandoned House(h), Magical Fields(f)")
            dest = input()
            print()

            if dest == 'e':
                spring_scene.print_forest(spring_scene.count)
                spring_scene.count += 1
                spring_scene.forest_scene()
                break
            elif dest == 'h':
                spring_scene.house_scene()
                break
            if dest == 'f':
                spring_scene.field_scene()
                break
            else:
                print('invalid input')

    investigated_house = False

    def house_scene():
        print("abandoned house")

        while True:
            if spring_scene.investigated_house:
                print("What would you like to do?\nInvestigate(i), Travel(t), Open Chest(c)")
            else:
                print("What would you like to do?\nInvestigate(i), Travel(t)")

            action = input()
            print()

            if action == 'i':
                if not spring_scene.investigated_house:
                    spring_scene.investigated_house = True
                    print("you found a chest with a lock")
                else:
                    print("nothing new")
                
            elif action == 't':
                break
            elif action == 'c':
                if spring_scene.found_key and not spring_scene.second_part:
                    spring_scene.second_part = True
                    print("you opened the chest and found the second part")
                elif spring_scene.second_part:
                    print("nothing else in the chest")
                else:
                    print("Hmm... seems like I need a key to open the chest.")
            else:
                print("action not known")

        while True:
            print("where would you like to go?\nOPTIONS: Enchanted Forest(e)")
            dest = input()
            print()

            if dest == 'e':
                spring_scene.forest_scene()
                break
            else:
                print("invalid input")

    investigated_garden = False
    has_shovel = False
    
    def garden_scene():
        print("garden of flowers")

        while True:
            if spring_scene.investigated_garden:
                print("What would you like to do?\nInvestigate(i), Travel(t), Dig Pile of Dirt(d)")
            else:
                print("What would you like to do?\nInvestigate(i), Travel(t)\n")
            
            action = input()
            print()

            if action == 'i':
                if not spring_scene.investigated_garden:
                    spring_scene.investigated_garden = True
                    print("found a pile of dirt and there seems to be a shed here.")
                else:
                    print("nothing new")
            elif action == 't':
                break
            elif action == 'd':
                if spring_scene.has_shovel and not spring_scene.third_part:
                    spring_scene.third_part = True
                    print("found the third part")
                elif spring_scene.third_part:
                    print("nothing else to dig")
                else:
                    print("cant dig the dirt pile. i need a tool to dig it up")
            else:
                print("invalid action")

        while True:
            if spring_scene.investigated_garden:
                print("where would you like to go?\nOPTIONS: Shed(s), Magical Fields(f)")
            else:
                print("where would you like to go?\nOPTIONS: Magical Fields(f)")
            dest = input()
            print()

            if dest == 'f':
                spring_scene.field_scene()
                break
            elif spring_scene.investigated_garden and dest == 's':
                spring_scene.shed_scene()
                break
            else:
                print("invalid option")

    investigated_shed = False
    def shed_scene():
        print("inside shed")

        while True:
            if spring_scene.investigated_shed and not spring_scene.has_shovel:
                print("What would you like to do?\nInvestigate(i), Travel(t), Pick up Rusty Shovel(s)")
            else:
                print("What would you like to do?\nInvestigate(i), Travel(t)")
            
            action = input()
            print()

            if action == 'i':
                if not spring_scene.investigated_shed:
                    spring_scene.investigated_shed = True
                    print("found a rusty shovel that looks like itll break")
                else:
                    print("nothing new")
            elif action == 't':
                break
            elif spring_scene.investigated_shed and action == 's':
                spring_scene.has_shovel = True
                print("pick up shovel and it turned brand new")
        
        while True:
            print("where would you like to go?\nOPTIONS: Flower Garden(g)")

            dest = input()
            print()

            if dest == 'g':
                spring_scene.garden_scene()
                break
            else:
                print("invalid option") 
        
    def ending_scene():
        print("")