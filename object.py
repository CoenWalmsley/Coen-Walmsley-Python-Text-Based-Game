from backpack import BackPack


class Object:

    def __init__(self, object_name, location):
        self.object_name = object_name
        self.location = location

    def collect_object(self, object_name):
        print(f"You have collected {self.object_name}.")
        BackPack.add(self.object_name, object_name)
