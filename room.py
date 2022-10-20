# Definition of the room class
class Room:
    def __init__(self, name, object_in_room, person_in_room, has_visited_room=False, user_input=None):
        """
        :param name: Name (string) of the room instance
        :param object_in_room: Boolean of whether there is an interactive object in room.
        :param person_in_room: Boolean of whether there is an interactive person in room.
        :param has_visited_room: Boolean of is user has visited room (default is False).
        """
        self.name = name
        self.object_in_room = object_in_room
        self.person_in_room = person_in_room
        self.has_visited_room = has_visited_room
        self.user_input = user_input

    def GetUserInput(self, name):
        user_input = input(f"You are currently in {name}, please press what you would like to do next: ")
        return user_input

    def LookAroundRoom(self, user_input="L"):
        if user_input == "L":
            print(f"In this room, you can see these objects: {object}")

    def GoNorth(self, user_input="N"):


