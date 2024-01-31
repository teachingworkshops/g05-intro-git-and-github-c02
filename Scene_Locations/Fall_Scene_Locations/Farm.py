import Locations
from User_Objects.Weapon import Weapon
from User_Objects.Armor import Armor
from User_Objects.Item import Item

from Characters.Story_Character import Story_Character

global SWORD_VALUE
SWORD_VALUE = 25

global SWORD_DAMAGE
SWORD_DAMAGE = 50

global COIN_AMOUNT
COIN_AMOUNT = 25

global CHEST_PLATE_VALUE
CHEST_PLATE_VALUE = 50

global CHEST_PLATE_PROTECTION_VALUE
CHEST_PLATE_PROTECTION_VALUE = 75

class Farm(Locations):
    def __init__(self, name):
        self.name = name
        self.discovered = False # Boolean

        # Create items to be found in barn
        sword = Weapon("Sword", "A weapon that deals damage to enemies.", True, SWORD_VALUE, SWORD_DAMAGE)
        gold_coins = Item("Gold Coins", "The currency used to buy and sell items.", False, COIN_AMOUNT)
        self.wood_chest = [sword, gold_coins]

        # Create items to be found in horse stable
        chest_plate = Armor("Chestplate", "Adds protection to any danger that approaches", True, CHEST_PLATE_VALUE, "chest", CHEST_PLATE_PROTECTION_VALUE)
        self.horse_stable_wall = [chest_plate]

        # Create story character
        self.farmer_bob = Story_Character("Farmer Bob")

        # Create sublocations

        # Child class of item, can reference item attributes and functions
        super().__init__(name, self.discovered)

    # Displays the items the player has in its backpack
    def display_backpack_items(self, main_character):
        print("")

    # Allows the player to inspect the barn
    def barn_sublocation(self, main_character):
        print("")

    # Allows the player to inspect the horse stable
    def horse_stable_sublocation(self, main_character):
        print("")

    # Displays available sublocations for the player to travel to
    def inspect_sublocations(self, traveler):
        # Create the sublocations
        barn = Barn("Barn", traveler)
        horse_stable = Horse_Stable("Horse Stable", traveler)
        corn_maze = Corn_Maze("Corn Maze", traveler)

        # Display sublocations
        print("Which location on the Farm would you like to explore?\n")
        print("[0]Barn\n")
        print("[1]Horse Stables\n")
        print("[2]Corn Maze\n")
        print("['q']Exit menu\n")
        response = input()

        # Match the response with action
        while response != 'q':
            if response == "0":
                barn.barn_scene()
            elif response == "1":
                horse_stable.horse_stable_scene()
            elif response == "2":
                corn_maze.corn_maze_scene()
            else:
                print("Invalid input.\n")

            print("Which location on the Farm would you like to explore?\n")
            print("[0]Barn\n")
            print("[1]Horse Stables\n")
            print("[2]Corn Maze\n")
            print("['q']Exit menu\n")

            response = input()

    # The dialogue between the player and farmer
    def farmer_dialogue(self, traveler):
        if self.farmer_bob.has_interacted:
            print("Welcome back!\n")
            print("Feel free to explore my farm and grab anything that maybe of use to you.\n")
        else:
            print("Hello there!\n")
            print(f"I am {self.farmer_bob.name}. What brings you around these parts?\n")

            while True:
                print("Enter response to Farmer Bob.\n")
                print(f"[0]My name is {traveler.name}. I am on a journey to explore the 4 seasons and take down the Timebro.")
                print(f"[1]I am a lost traveler seeking supplies")
                response_1 = input()
                if response_1 == "0":
                    print("Wow, I've heard frightening things about the Timebro.") 
                    print("Feel free to look around my farm if there is anything that interests you, please have.\n")
                    break
                elif response_1 == "1":
                    print("I am sorry to hear that. I have supplies that might be of interest in my barn and horse stable.\n")
                    break
                else:
                    print("Invalid input.\n")

    # Beginning of the farm scene
    def location_scene(self, main_character):
        print("You have successfully traveled to the farm.")
        print("Available commands:")
        self.discovered = True
        action = input("[0]Approach farmer\n['i']Inspect sublocations\n['b']Open backpack\n['q']Leave Farm")
        while action != "q":
            if action == "0":
                self.farmer_dialogue()
            elif action == "i":
                self.inspect_sublocations()
            elif action == "b":
                self.display_backpack_items(main_character)
            else:
                print("Invalid input.\n")

            action = input("[0]Approach farmer\n['i']Inspect sublocations\n['b']Open backpack\n['q']Leave location")

class Barn(Farm):
    def __init__(self, name, traveler):
        self.name = name
        self.traveler = traveler

        # Child class of item, can reference item attributes and functions
        super().__init__(name, self.discovered)

    def barn_scene(self):
        print("The barn's weathered door opened, revealing a vast expanse filled with the comforting scents of hay and aged wood.\n")
        print("Sunlight beamed on the worn floor, highlighting stalls where animals ate.\n")
        print("There were tall stacks of haybales and next to the haybales a wooden chest.\n")

        print("Do you open the chest?\n")
        print("['y']Yes\n")
        print("['n']No\n")
        print("['q']Leave barn\n")

        response = input()

        while True:
            if response == 'y':
                print("")
                break
            elif response == 'n':
                print("")
                break
            elif response == 'q':
                break
            else:
                print("Invalid response.\n")

class Horse_Stable(Farm):
    def __init__(self, name):
        self.name = name

        # Child class of item, can reference item attributes and functions
        super().__init__(name, self.discovered)
    
    def horse_stable_scene(self):
        print("")

class Corn_Maze(Farm):
    def __init_(self, name):
        self.name = name

        # Child class of item, can reference item attributes and functions
        super().__init__(name, self.discovered)

    def corn_maze_scene(self):
        print("")


            
