from Scene_Locations.Locations import Locations

class Great_Pumpkin(Locations):
    def __init__(self, name):
        self.name = name
        self.discovered = False
        self.completed = False

        # Child class of item, can reference item attributes and functions
        super().__init__(name, self.discovered)

    def location_scene(self, traveler):
        print("You have approached the Great Pumpkin.\n")
        print("No traveler has been able to cross the bridge due to the Great Pumpkin that blocks it.\n")
        print("You must find a way to bring down the Great Pumpkin to cross the bridge to get to the next season.\n")


    def end_scene(self, traveler):
        print("Your magical animals help pave a path through the Great Pumpkin, which allows you to cross the bridge into the next season, winter.\n")
        self.completed = True