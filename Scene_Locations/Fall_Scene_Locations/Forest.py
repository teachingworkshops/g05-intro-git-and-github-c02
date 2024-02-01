from Scene_Locations.Locations import Location

from Characters.Story_Character import StoryCharacter
from Characters.Main_Character import MainCharacter

from User_Objects.Weapon import Weapon

class Forest(Location):
    def __init__(self, name, great_pumpkin):
        self.name = name
        self.discovered = False
        self.great_pumpkin = great_pumpkin

        # Create minions
        self.small_minion = StoryCharacter("Small Minion")
        self.large_minion = StoryCharacter("Large Minion")

        # Child class of item, can reference item attributes and functions
        super().__init__(name, self.discovered)

    def location_scene(self, traveler: MainCharacter):
        print("As you enter the forest, you follow a dirt path.\n")
        # Checks to see if this has been completed already
        if not self.small_minion.has_interacted and not self.large_minion.has_interacted:
            while not self.great_pumpkin.completed:
                print("You find wood wheel tracks and horse prints, as you look up you see two of Timebro's minions riding a horse carriage.\n\n")

                print("[0]Confront Timebro's minions\n")
                print("[1]Run away to a different location\n")

                response_1 = input("Choose the number corresponding to the action you want to perform.\n")

                if response_1 == "0":
                    print("The minions hault the carriage.\n")
                    print("Both minions draw out there swords.\n")
                    print("One minion has a sword that deals 25 damage.\n")
                    print("The other minion has a sword that deals 45 damage.\n")

                    print("[0]Fight the minions\n")
                    print("[1]Leave the Forrest\n")

                    response_2 = input("\nChoose an action to perform.\n")

                    if response_2 == "0":
                        print("Your weapons:\n")
                        count = 0
                        for index, item in enumerate(traveler.backpack.backpack_storage):
                            if type(item) == Weapon:
                                print(f"[{index}] {item.name}       description: {item.description}\n")
                                count += 1

                        if count > 0:
                            while True:
                                try:
                                    index = input("Choose your weapon by typing the corresponding index.\n")
                                    weapon_chosen = traveler.backpack.backpack_storage[int(index)]

                                    print(f"You chose the {weapon_chosen.name}\n")
                                    print(f"Your {weapon_chosen.name} does {weapon_chosen.damage}")
                                    if weapon_chosen.damage < 25:
                                        print("Your weapon does not do enough damage. You run away.\n")
                                        break
                                    elif weapon_chosen.damage < 45:
                                        print("Your weapon does not have enough damage to take on both minions. You run away.\n")
                                    else:
                                        print("Your weapon does enough damage. You won the fight and took down both minions!\n")
                                        # Update the minions has interacted with player success
                                        self.small_minion.has_interacted = True
                                        self.large_minion.has_interacted = True

                                        print("You notice in the back of the carriage, there are magical animals stuck in a cage.")
                                        if len(traveler.backpack.key_storage) > 0:
                                            print("You use the key that you found, to unlock the cage.\n")

                                        print("The magical animals have agreed to help you get passed the Great Pumpkin as a thanks for saving them.\n")
                                        self.great_pumpkin.end_scene(traveler)
                                        break

                                except IndexError: 
                                    print("Invalid input.\n")
                                except Exception as exp:
                                    print(exp)

                        else:
                            print("You have no weapon to fight with. You run away.\n")
                            break
                    elif response_2 == "1":
                        break
                    else:
                        print("Invalid input\n") 
                elif response_1 == "1":
                    break
                else:
                    print("Invalid response.\n")
        else:
            print("You have already defeated the minions and have set the magic animals free.\n")
            print("You travel to the Great Pumpkin.")
            self.great_pumpkin.end_scene(traveler)






    