# Call methods from each scene
# When each scene has been completed the method for the next scene is called

from Scenes.FallScene import fall_scene
from Scenes.WinterScene import winter_scene
from Scenes.SpringScene import spring_scene
from Scenes.SummerScene import summer_scene


from Characters.Main_Character import MainCharacter

# Main function to run story game
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
    main()