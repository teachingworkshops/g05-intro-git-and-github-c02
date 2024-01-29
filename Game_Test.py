# Call methods from each scene
# When each scene has been completed the method for the next scene is called

from Scenes.FallScene import fall_scene

def main():
    fall_scene.run_scene()

if __name__ == "__main__":
    main()