# Location class

class location:
    def __init__(self, name: str):
        self.name = name
        self.discovered = False

        # A list of sublocations 
        # For instance, I was thinking if there are things to do at a location can be kept track here
        # Ex. for Fall scene, a location I have is a farm and then at the farm there is a horse stable and a corn maze
        self.sub_location = []

    class sub_location:
        def __init__(self, name: str):
            self.name = name
            self.discovered = False