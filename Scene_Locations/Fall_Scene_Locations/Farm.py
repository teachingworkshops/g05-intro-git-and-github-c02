from Scene_Locations.Locations import Location
from User_Objects.Weapon import Weapon
from User_Objects.Armor import Armor
from User_Objects.Item import Item
from User_Objects.Key import Key

from Characters.Main_Character import MainCharacter
from Characters.Story_Character import StoryCharacter

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

class Farm(Location):
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
        self.farmer_bob = StoryCharacter("Farmer Bob")

        # Create sublocations

        # Child class of item, can reference item attributes and functions
        super().__init__(name, self.discovered)

    # Displays the items the player has in its backpack
    def display_backpack_items(self, traveler: MainCharacter):
        # Print the backpack storage
        print("Inside the backpack storage:\n")
        for item in traveler.backpack.backpack_storage:
            print(f"{item.name}       description: {item.description}       value: {item.cost_value}\n")

        # Print amount of coins the player has
        print(f"You have {traveler.coin_storage} coins.\n")

        # Print the keys found
        count = 0
        for item in traveler.backpack.key_storage:
            print(f"{item.name}       description: {item.description}       value: {item.cost_value}\n")
            count += 1
        if count == 0:
            print("You don't have any keys at the moment.\n")

        # Print the maps found
        count = 0
        for item in traveler.backpack.map_storage:
            print(f"{item.name}       description: {item.description}       value: {item.cost_value}\n")
            count += 1
        if count == 0:
            print("You don't have any maps at the moment.\n")

    # Displays available sublocations for the player to travel to
    def inspect_sublocations(self, traveler):
        # Create the sublocations
        barn = Barn("Barn", traveler, self)
        horse_stable = Horse_Stable("Horse Stable", traveler, self)
        corn_maze = Corn_Maze("Corn Maze", traveler, self)

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
            print("\nWelcome back!\n")
            print("Feel free to explore my farm and grab anything that maybe of use to you.\n")
        else:
            print("Hello there!\n")
            print(f"I am {self.farmer_bob.name}. What brings you around these parts?\n")

            while True:
                print("Enter response to Farmer Bob.\n")
                print(f"[0]My name is {traveler.name}. I am on a journey to explore the 4 seasons and take down the Timebro.")
                print(f"[1]I am a lost traveler seeking supplies.\n")
                response_1 = input()
                if response_1 == "0":
                    print("Wow, I've heard frightening things about the Timebro.") 
                    print("Feel free to look around my farm if there is anything that interests you, please have.\n")
                    self.farmer_bob.has_interacted = True
                    break
                elif response_1 == "1":
                    print("I am sorry to hear that. I have supplies that might be of interest in my barn and horse stable.\n")
                    self.farmer_bob.has_interacted = True
                    break
                else:
                    print("Invalid input.\n")

    # Beginning of the farm scene
    def location_scene(self, traveler):
        print("You have successfully traveled to the farm.")
        print("Available commands:")
        self.discovered = True
        action = input("[0]Approach farmer\n['i']Inspect sublocations\n['b']Open backpack\n['q']Leave Farm\n")
        while action != "q":
            if action == "0":
                self.farmer_dialogue(traveler)
            elif action == "i":
                self.inspect_sublocations(traveler)
            elif action == "b":
                self.display_backpack_items(traveler)
            else:
                print("Invalid input.\n")

            action = input("[0]Approach farmer\n['i']Inspect sublocations\n['b']Open backpack\n['q']Leave location\n")

class Barn():
    def __init__(self, name, traveler: MainCharacter, farm: Farm):
        self.name = name
        self.traveler = traveler
        self.farm = farm
        self.completed = False

    def barn_scene(self):
        print("\nThe barn's weathered door opened, revealing a vast expanse filled with the comforting scents of hay and aged wood.\n")
        print("Sunlight beamed on the worn floor, highlighting stalls where animals ate.\n")
        print("There were tall stacks of haybales and next to the haybales a wooden chest.\n")
        if not self.completed:

            print("Do you open the chest?\n")
            print("['y']Yes\n")
            print("['n']No\n")
            print("['q']Leave barn\n")

            response_1 = input()

            while True:
                if response_1 == 'y':
                    print("Inside the wooden chest:\n\n")
                    for index, item in enumerate(self.farm.wood_chest):
                        print(f"[{index}] {item.name}       description: {item.description}       value: {item.cost_value}\n")
                    
                    print(f"\n[{index+1}]Take all\n")
                    print(f"\n[{index+2}]Exit wooden chest\n")

                    response_2 = input("Input a number value corresponding to an item you'd like to take.\n")

                    # While there are things in the wood chest and the user has not decided to leave the wooden chest
                    while len(self.farm.wood_chest) > 0 and response_2 != str(index+2):
                        try:
                            if response_2 == str(index+1):
                                for index, item in enumerate(self.farm.wood_chest):
                                    # Adds item chose to the backpack
                                    item = self.farm.wood_chest[index]
                                    if item.name == "Gold Coins":
                                        self.traveler.coin_storage += item.cost_value
                                    else:
                                        self.traveler.backpack.backpack_storage.append(item)
                                # Remove all items from the wood chest
                                self.farm.wood_chest.clear()
                            else:
                                # Adds item chose to the backpack
                                item = self.farm.wood_chest[int(response_2)]
                                if item.name == "Gold Coins":
                                    self.traveler.coin_storage += item.cost_value
                                else:
                                    self.traveler.backpack.backpack_storage.append(item)
                                # Remove item from the wood chest
                                self.farm.wood_chest.remove(item)

                        except IndexError: 
                            print("Invalid input.\n\n")
                            i = i-1
                        except Exception as exp:
                            print(exp)

                        if len(self.traveler.backpack.backpack_storage) > self.traveler.backpack.storage_val:
                            remove_item_num = len(self.traveler.backpack.backpack_storage) - self.traveler.backpack.storage_val
                            print(f"You have {remove_item_num} to many items in your bag.")
                            self.farm.display_backpack_items()
                            
                            for i in range(remove_item_num):
                                try:
                                    response_3 = input("Enter the number corresponding to the item youd like to remove")
                                    remove_item = self.traveler.backpack.backpack_storage[response_3]
                                    self.traveler.backpack.backpack_storage.remove(remove_item)

                                    self.farm.display_backpack_items()
                                except IndexError: 
                                    print("Invalid input.\n\n")
                                    i = i-1
                                except Exception as exp:
                                    print(exp)

                        print("Inside the wooden chest:\n\n")
                        count = 0
                        for index, item in enumerate(self.farm.wood_chest):
                            print(f"[{index}] {item.name}       description: {item.description}       value: {item.cost_value}\n")
                            count += 1
                        if count > 0:
                            print(f"\n[{index+1}]Take all\n")
                        print(f"\n[{index+2}]Exit wooden chest\n")

                        response_2 = input("Input a number value corresponding to an item you'd like to take.\n")
                    self.completed = True
                    break
                elif response_1 == 'n':
                    print("If you choose to check out items at a later time. You can go back.\n")
                    break
                elif response_1 == 'q':
                    break
                else:
                    print("Invalid response.\n")

        else:
            print("There is nothing left to find in the barn.\n")

class Horse_Stable():
    def __init__(self, name: str, traveler: MainCharacter, farm: Farm):
        self.name = name
        self.traveler = traveler
        self.farm = farm
    
    def horse_stable_scene(self):
        print("The horse stables had an interesting smell.\n")
        print("There were many horses inside eating and sleeping.\n")
        while True:
            # Check if it is the first time
            if len(self.farm.horse_stable_wall) > 0:
                print("Off to the side there hanging on the wall was some chest plate armor.\n")

                print("Do you take the chest plate armor?\n")

                # Add print of description of the chest plate
                print("['y']Yes\n")
                print("['n']No\n")
                print("['q']Leave horse stables\n")

                response_1 = input()
                if response_1 == 'y':
                    if self.traveler.armor_dict["chest"] == "":
                        # Adds the armor to player
                        self.traveler.armor_dict[self.farm.horse_stable_wall[0].armor_type] = self.farm.horse_stable_wall[0]
                        # Need to update health points
                        self.traveler.update_health_points(self.farm.horse_stable_wall[0])
                        # Remove the armor from the wall
                        self.farm.horse_stable_wall.remove(self.farm.horse_stable_wall[0])
                        print("You have taken and put on the chest plate armor.\n")
                elif response_1 == 'n':
                    pass
                elif response_1 == 'q':
                    break # Leaves horse stables
            else: # Nothing left to do in barn stable if armor has been taken
                response_2 = input("['q']Leave horse stables\n")
                while response_2 != 'q':
                    print("Invalid response.\n")
                    response_2 = input("['q']Leave horse stables\n")
                break # Leaves horse stables

class Corn_Maze():
    def __init__(self, name: str, traveler: MainCharacter, farm: Farm):
        self.name = name
        self.traveler = traveler
        self.farm = farm

    def corn_maze_scene(self):
        print("The tall corn was taller than me.\n")
        print("The corn was super yellow.\n")

        # Create minion
        minion = StoryCharacter("Minion")

        while not minion.has_interacted:
            print("And then a bad guy approaches, a minion of Timebro!\n")

            print("[0]Fight the minion\n")
            print("[1]Leave the corn maze\n")

            response_1 = input("\nChoose an action to perform.\n")

            if response_1 == "0":
                print("Your weapons:\n")
                count = 0
                for index, item in enumerate(self.traveler.backpack.backpack_storage):
                    if type(item) == Weapon:
                        print(f"[{index}] {item.name}       description: {item.description}\n")
                        count += 1

                if count > 0:
                    while True:
                        try:
                            print("The minion does 15 damage, choose a weapon that does more than 15 damage.")
                            index = input("Choose your weapon by typing the corresponding index.\n")
                            weapon_chosen = self.traveler.backpack.backpack_storage[int(index)]

                            print(f"You chose the {weapon_chosen.name}\n")
                            print(f"Your {weapon_chosen.name} does {weapon_chosen.damage}")
                            if weapon_chosen.damage < 15:
                                print("Your weapon does not do enough damage. You run away.\n")
                                break
                            else:
                                print("Your weapon does enough damage. You won the fight!\n")
                                print("You find a key on the minion and put it in your backpack\n")
                                key = Key("Fall Season Key", "A key can be held onto and used during different parts of the season.", False, 100)
                                self.traveler.backpack.key_storage.append(key) # Adds key to traveler

                                # Update that the minion has interacted with player successfully
                                minion.has_interacted = True

                                break

                        except IndexError: 
                            print("Invalid input.\n")
                        except Exception as exp:
                            print(exp)

                else:
                    print("You have no weapon to fight with. You run away.\n")
                    break
            elif response_1 == "1":
                break
            else:
                print("Invalid input\n") 


            
