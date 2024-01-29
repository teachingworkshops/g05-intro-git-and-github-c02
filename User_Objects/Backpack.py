# Backpack class
class backpack:
    def __init__(self, storage_val):
        self.storage_val = storage_val

        # List of objects in the characters backpack (not including maps and keys)
        self.backpack_storage = []

        # List of map objects
        self.map_storage = []

        # List of key objects
        self.key_storage = []