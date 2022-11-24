class Object:
    def __init__(self, object_name, location):
        """

        :param object_name: The name of the object.
        :param location:  The room location of where the object is.
        """
        self.object_name = object_name
        self.location = location

# Allows the player to collect the object.
    def collect_object(self):
        print(f"You have collected {self.object_name}.")
