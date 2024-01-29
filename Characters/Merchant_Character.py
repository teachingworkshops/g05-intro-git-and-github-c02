# Merchant class
from .Main_Character import MainCharacter

# Merchant can sell items
# Do we want the ability to sell items to the merchant?
class Merchant:
    def __init__(self, store_items: list):
        # When an item is bought can remove the item from the list
        # Each item in the list has a cost
        self.store_items = store_items

    # Called in the merchant dialogue
    def display_store(self):
        for index, item in enumerate(self.store_items):
            print(f"[{index}] {item.name}       cost: {item.cost_value} coins\n")

    # Everytime the main character meets a merchant, this function can be called
    # This function displays the store based on the item the merchant has
    # Subtracts the amount of gold the main character has when something is bought
    # Adds the item to the main character's backpack once an item is bought
    def merchant_dialogue(self, main_character: MainCharacter):

        print("Hello! I am a traveling merchant.\n")
        print("Here is what I have available\n")
        self.display_store()

        item_input = input("\nIs there anything that interests you? Enter 'q' to leave the store.\n")
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
                        # Subtracks the amount of coins the main character has
                        main_character.coin_storage = main_character.coin_storage - item.cost_value
                        # Adds the bought item to the character's backpack
                        main_character.backpack.backpack_storage.append(item)
                        print(f"Here is your {item.name}. Thank you for your business!\n\n")
                # If the main character doesn't want to buy the item of interest
                else:
                    print("\n")

                self.display_store()

                item_input = input("\nIs there something else that interests you? Enter 'q' to leave the store.\n")

            # If there is an exception, the input number is not an index for one of the items  
            except IndexError: 
                print("Unfortunately, I do not have the item you requested.\n\n")
                self.display_store()

                item_input = input("\nIs there something else that interests you? Enter 'q' to leave the store.\n")
            except Exception as exp:
                print(exp)   

        print("\nThank you for stopping by! Goodluck on your journey!\n")

        


