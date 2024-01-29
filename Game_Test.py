# Call methods from each scene
# When each scene has been completed the method for the next scene is called

from Scenes.FallScene import fall_scene

from Characters.Main_Character import main_character

def main():
    #while True:
    traveler = main_character(input("What is your name?\n"))
    print("Good luck, " +traveler.name+ ".")
    fall_scene.run_scene()

if __name__ == "__main__":
    main()