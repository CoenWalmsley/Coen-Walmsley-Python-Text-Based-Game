from person import Person
from object import Object

class Room:
    user_input = ""
    has_visited_room = False

    def __init__(self, name, object_in_room, person_in_room, north_room, south_room, east_room, west_room,
                 has_visited_room):

        self.name = name
        self.object_in_room = object_in_room
        self.person_in_room = person_in_room

        self.north_room = north_room
        self.south_room = south_room
        self.west_room = west_room
        self.east_room = east_room
        self.has_visited_room = has_visited_room
    def get_user_input(self, name):
        user_input = input(f"You are currently in {name}, please press what you would like to do next: ")
        return user_input

    def look_around_room(self, object_in_room, person_in_room, user_input):
        Room.has_visited_room = True
        if object_in_room:
            print(f"In this room, you can see these objects: {object}")
        else:
            print("There are no objects in this room.")

        if person_in_room:
            print(f"In this room, you can see {user_input}")
        else:
            print("There is no one else in this room.")

    def GoNorth(self, user_input, north_room):
        if north_room == None:
            print("You cannot travel North, try another command.")
            return


    def GoSouth(self, user_input, south_room):
        if south_room == None:
            print("You cannot travel South, try another command.")
            return


