# Call methods from each scene
# When each scene has been completed the method for the next scene is called

from Scenes.FallScene import fall_scene

from Characters.Main_Character import MainCharacter

# Main function to run story game
def main():
    #while True:
    traveler = MainCharacter(input("What is your name?\n"))
    # Describe overall description and objective of the game
    # Describe basic controls for the main character, 
        # view objects in backpack, 
        # how to move to different locations, 
        # view amount of coins you have
        # view map?



    print("Good luck, " +traveler.name+ ".")
    fall_scene.run_scene(traveler)
    # Add functions to run other scenes

if __name__ == "__main__":
    main()