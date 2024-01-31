# Merchant class
from .Main_Character import MainCharacter
from User_Objects.Backpack import Backpack

# Merchant can sell items
# Do we want the ability to sell items to the merchant?
class Merchant:
    def __init__(self, store_items: list):
        # When an item is bought can remove the item from the list
        # Each item in the list has a cost
        self.store_items = store_items

    # Called in the merchant dialogue
    # Displays all of the items the merchant has to offer as well as the cost value
    # If the player chooses to have interest in an item the description and additional information will be shown
    def display_items(self, items: list):
        count = 0 # To see how many items are printed, could have items in backpack but arent sellable
        for index, item in enumerate(items):
            if item.can_sell:
                print(f"[{index}] {item.name}       cost: {item.cost_value} coins\n")
                count += 1

        if count == 0:
            print("You do not have any items in your backpack that can be sold.\n")

        return count

    # Displays the items the player has that can be sold
    # If an item is sold, coin is added to the player, and the item is removed from the backpack
    def sell_item_action(self, main_character: MainCharacter):
        print("Here are the items you have that you can sell:\n")
        
        count = self.display_items(main_character.backpack.backpack_storage)
        if count > 0:
            item_input = input("\nIs there anything that you want to sell? Enter 'q' to leave this menu.\n")
            while item_input != 'q':
                # Present more information on the object of interest
                try:
                    item_index = int(item_input)
                    item = self.store_items[item_index]

                    print("\nAh yes of course!\n")
                    print(f"\n{item.name} description: {item.description}\n")

                    sell_item = input(f"\nWould you like to sell this item for {item.cost_value} coins? Enter ['y'] or ['n'].\n")
                    while sell_item != 'y' and sell_item != 'n':
                        # If the main character inputs an answer that is not 'y' or 'n'
                        print("I didn't catch that answer.\n")
                        buy_item = input(f"\nWould you like to sell this item for {item.cost_value}? Enter ['y'] or ['n'].\n")

                    # If the main character wants to sell the item of interest
                    if sell_item == 'y':
                        # Adds the coins to the player
                        main_character.coin_storage = main_character.coin_storage + item.cost_value
                        # Removes the sold item to the character's backpack
                        main_character.backpack.backpack_storage.remove(item)
                        print(f"You now have {main_character.coin_storage} coins.\n")
                        print(f"Thank you for your business!\n\n")
                    # If the main character doesn't want to buy the item of interest
                    else:
                        print("\n")

                    count = self.display_items(main_character.backpack.backpack_storage)
                    if count > 0:
                        item_input = input("\nIs there anything else you want to sell? Enter 'q' to leave this menu.\n")

                # If there is an exception, the input number is not an index for one of the items  
                except IndexError: 
                    print("Unfortunately, I do not have the item you requested.\n\n")
                    count = self.display_items(main_character.backpack.backpack_storage)
                    if count > 0:
                        item_input = input("\nIs there anything else you want to sell? Enter 'q' to leave this menu.\n")
                except Exception as exp:
                    print(exp)

    
    # This function displays the store based on the item the merchant has
    # Subtracts the amount of gold the main character has when something is bought
    # Adds the item to the main character's backpack once an item is bought
    def buy_item_action(self, main_character: MainCharacter):
        print("Here is what I have available\n")
        count = self.display_items(self.store_items)

        item_input = input("\nIs there anything that interests you? Enter 'q' to leave this menu.\n")
        while item_input != 'q':
            # Present more information on the object of interest
            try:
                item_index = int(item_input)
                item = self.store_items[item_index]

                print("\nAh yes of course!\n")
                print(f"\n{item.name} description: {item.description}\n")

                print(f"You have {main_character.coin_storage} coins.")
                buy_item = input(f"\nWould you like to purchase this item for {item.cost_value}? Enter ['y'] or ['n'].\n")
                while buy_item != 'y' and buy_item != 'n':
                    # If the main character inputs an answer that is not 'y' or 'n'
                    print("I didn't catch that answer.\n")
                    print(f"You have {main_character.coin_storage} coins.")
                    buy_item = input(f"\nWould you like to purchase this item for {item.cost_value}? Enter ['y'] or ['n'].\n")

                # If the main character wants to buy the item of interest
                if buy_item == 'y':
                    # Checks that you have enough coin to purchase item
                    if main_character.coin_storage - item.cost_value < 0:
                        print("You do not have enough coins to purchase this item.\n")
                    else:
                        # A backpack doesn't need to be added inside a backpack, just updates the player's backpack with the new storage value
                        if type(item) == Backpack:
                            # Updates the new storage value of the backpack
                            main_character.backpack.storage_val = item.storage_val 
                        else: 
                            # Adds the bought item to the character's backpack
                            main_character.backpack.backpack_storage.append(item)

                        # Subtracts the amount of coins the main character has
                        main_character.coin_storage = main_character.coin_storage - item.cost_value
                        
                        self.store_items.remove(item) # Removes item from the store since it has been purchased
                        print(f"Here is your {item.name}. Thank you for your business!\n\n")

                # If the main character doesn't want to buy the item of interest
                else:
                    print("\n")

                count = self.display_items(self.store_items)
                if count > 0:
                    item_input = input("\nIs there something else that interests you? Enter 'q' to leave this menu.\n")

            # If there is an exception, the input number is not an index for one of the items  
            except IndexError: 
                print("Unfortunately, I do not have the item you requested.\n\n")
                count = self.display_items(self.store_items)
                if count > 0:
                    item_input = input("\nIs there something else that interests you? Enter 'q' to leave the menu.\n")
            except Exception as exp:
                print(exp)

    # Everytime the main character meets a merchant, this function can be called
    # The player will choose between leaving the merchant to move on, sell item(s) or buy item(s)
    def merchant_dialogue(self, main_character: MainCharacter):

        print("Hello! I am a traveling merchant.\n")

        first_action = input("Would you like to: \n[0]sell item(s) \n[1]buy item(s) \n['q']quit \n\nType the value associated with the action.\n")
        
        while(first_action != 'q'): # Allows for the player to sell items and buy items back and forther and multiple times
            if first_action == '0': # Present the items the user can sell
                self.sell_item_action(main_character)
            elif first_action == '1': # Present the items available at the merchant
                self.buy_item_action(main_character)
            elif first_action == 'q': # Skip to the end of the merchant's dialogue to continue with the game
                break # exits while loop
            else: # If any other character was input
                print("Sorry I didn't understand that")

            first_action = input("Would you like to: \n[0]sell item(s) \n[1]buy item(s)? \n['q']quit \n\nType the value associated with the action.\n")

        print("\nThank you for stopping by! Goodluck on your journey!\n")

        


