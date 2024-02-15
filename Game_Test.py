# Call methods from each scene
# When each scene has been completed the method for the next scene is called

from Scenes.FallScene import fall_scene
from Scenes.WinterScene import winter_scene
from Scenes.SpringScene import spring_scene
from Scenes.SummerScene import summer_scene


from Characters.Main_Character import MainCharacter


def display_start_menu():
    print("Welcome to: ")
    print("""
_____  ____  _     _____   ____  _____   _____  _  _      _____
/__ __\/  _ \/ \   /  __/  /  _ \/    /  /__ __\/ \/ \__/|/  __/
  / \  | / \|| |   |  \    | / \||  __\    / \  | || |\/|||  \  
  | |  | |-||| |_/\|  /_   | \_/|| |       | |  | || |  |||  /_ 
  \_/  \_/ \|\____/\____\  \____/\_/       \_/  \_/\_/  \|\____\    """)
    
    print("\n[1] Start Game")
    print("[2] Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Starting game...")
        main()  
    elif choice == "2":
        print("Quitting game. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        display_start_menu()

def main():

    print("Hello traveler!\n")
    traveler = MainCharacter(input("What is your name?\n"))
    print("In this game you will be able to explore the 4 seasons and pick up items along to way to ultimately defeat the Timebro.\n")

    print("Good luck, " +traveler.name+ ".\n")
    fall = fall_scene()
    fall.run_scene(traveler)

    winter = winter_scene()
    winter.run_scene(traveler)

    spring = spring_scene()
    spring.run_scene()

    summer = summer_scene
    summer.run_scene(traveler)
    # Add functions to run other scenes

if __name__ == "__main__":
    display_start_menu()