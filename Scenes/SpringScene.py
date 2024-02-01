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
            print("The enchanted forest is filled with beauty. But you have a strange feeling about this place.")

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
                    print("A shiny light appeared! Perhaps there is something there...")
                else:
                    print("There seems to be nothing around. It looks like you can keep going.")
            elif action == 't':
                break
            elif spring_scene.count >= 3 and action == 'l':
                if not spring_scene.found_key:
                    spring_scene.found_key = True
                    print("You found a key! Wonder what that is for...")
                else:
                    print("There is nothing else in the light.")
            else:
                print("This action is not known.")

        while True:
            print("Where would you like to go?\nOPTIONS: Deeper into the Enchanted Forest(e), Abandoned House(h), Magical Fields(f)")
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
                print('This place is not known.')

    investigated_house = False

    def house_scene():
        print("The old wooden house looks like it has been abandoned for years. There is debris everywhere.")

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
                    print("You found a chest! But it is locked... I need a key inorder to open it.")
                else:
                    print("There is nothing new.")
                
            elif action == 't':
                break
            elif action == 'c':
                if spring_scene.found_key and not spring_scene.second_part:
                    spring_scene.second_part = True
                    print("You opened the chest and found the second piece of the spell!")
                elif spring_scene.second_part:
                    print("There is nothing else in the chest.")
                else:
                    print("Hmm... seems like I need a key to open the chest.")
            else:
                print("This action is not known.")

        while True:
            print("Where would you like to go?\nOPTIONS: Enchanted Forest(e)")
            dest = input()
            print()

            if dest == 'e':
                spring_scene.forest_scene()
                break
            else:
                print("This place is unknown.")

    investigated_garden = False
    has_shovel = False
    
    def garden_scene():

        if not spring_scene.third_part:
            print("The garden is filled with blooming flowers of all sizes and colors. Some of them are singing and dancing,")
            print("but there are some that are stuck.")
        else:
            print("The garden is filled with blooming flowers of all sizes and colors. All of them singing and dancing in harmony")
            
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
                    print("There seems to be a pile of strange dirt, and there seems to be a shed here too.")
                else:
                    print("There is nothing new.")
            elif action == 't':
                break
            elif action == 'd':
                if spring_scene.has_shovel and not spring_scene.third_part:
                    spring_scene.third_part = True
                    print("You dig up the strange dirt with the shovel and found the third piece of the spell!")
                elif spring_scene.third_part:
                    print("There is nothing else to dig.")
                else:
                    print("You can't dig the strange dirt. Looks like you need a tool to help you.")
            else:
                print("This action is not known.")

        while True:
            if spring_scene.investigated_garden:
                print("Where would you like to go?\nOPTIONS: Shed(s), Magical Fields(f)")
            else:
                print("Where would you like to go?\nOPTIONS: Magical Fields(f)")
            dest = input()
            print()

            if dest == 'f':
                spring_scene.field_scene()
                break
            elif spring_scene.investigated_garden and dest == 's':
                spring_scene.shed_scene()
                break
            else:
                print("This place is not known.")

    investigated_shed = False
    def shed_scene():
        print("The shed is filled with old and rusted tools. Surely these weren't used for this garden...")

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
                    print("You found a rusty shovel, but it looks like it will break at a single touch.")
                else:
                    print("There is nothing new.")
            elif action == 't':
                break
            elif spring_scene.investigated_shed and action == 's':
                spring_scene.has_shovel = True
                print("You pick up the rusty shovel, and it transfoms into an elegant and shiny shovel!")
            else:
                print("This action is not known.")
        
        while True:
            print("Where would you like to go?\nOPTIONS: Flower Garden(g)")

            dest = input()
            print()

            if dest == 'g':
                spring_scene.garden_scene()
                break
            else:
                print("This place is not known.") 
        
    def ending_scene():
        print("The spell brings the wall of vines down. You see the next challenge you must face. You move forward knowing")
        print("what has to be done.")