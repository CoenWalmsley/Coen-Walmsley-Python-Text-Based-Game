class Object:

    inventory = []

    def __init__(self, object_name, location):
        self.object_name = object_name
        self.location = location

    def collect_object(self):
        print(f"You have collected {self.object_name}.")
        self.inventory.append(self.object_name)
        return self.inventory
