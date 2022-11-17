class Room:
    def __init__(self, name, room_number, object_in_room=False, person_in_room=False):
        """

        :param name: The name of the room.
        :param room_number: The number of the room on the map.
        :param object_in_room: Boolean value of whether there is an object in the room or not.
        :param person_in_room: Boolean value of whether there is a person in the room or not.
        """
        self.name = name
        self.room_number = room_number
        self.object_in_room = object_in_room
        self.person_in_room = person_in_room

    def look_around_room(self):
        if self.object_in_room is True:
            print(f"In this room, you've spotted an object, press G to grab.")
            self.object_in_room = False
        if self.person_in_room:
            print(f"You found someone, press T to talk to them.")
        else:
            print("There are no objects in this room.")


class RoomMapping(Room):
    def __init__(self, north_room, south_room, east_room, west_room, object, person, name, room_number):
        super().__init__(name, room_number)
        self.north_room = north_room
        self.south_room = south_room
        self.east_room = east_room
        self.west_room = west_room
        self.object= object
        self.person = person

    def move_room(self):
        user_input = input("Enter your next move: ")
        if user_input == "N":
            north_room = self.north_room
            if north_room is not None:
                current_room = north_room
                print(f"You are now in {current_room.name}.")
                return current_room
            else:
                print("No room found, please travel another direction.")
                return
        elif user_input == "S":
            south_room = self.south_room
            if south_room is not None:
                current_room = south_room
                print(f"You are now in {current_room.name}.")
                return current_room
            else:
                print("No room found, please travel another direction.")
                return
        elif user_input == "E":
            east_room = self.east_room
            if east_room is not None:
                current_room = east_room
                print(f"You are now in {current_room.name}.")
                return current_room
            else:
                print("No room found, please travel another direction.")
                return
        elif user_input == "W":
            west_room = self.west_room
            if west_room is not None:
                current_room = west_room
                print(f"You are now in {current_room.name}.")
                return current_room
            else:
                print("No room found, please travel another direction.")
                return


main_entrance = Room("Main Entrance", 0, True, False)
lobby = Room("Lobby", 1, False, True)
bedroom_one = Room("Bedroom One", 2, True, False)
ensuite = Room("Ensuite", 3, True, False)
dining = Room("Dining", 4, True, False)
bedroom_two = Room("Bedroom Two", 5, True, False)
living = Room("Living", 6, False, True)
kitchen = Room("Kitchen", 7, True, False)
butler_quarters = Room("Butler Quarters", 8, True, True)
courtyard = Room("Courtyard", 9, True, False)
bar = Room("Bar", 10, True, False)
bathroom = Room("Bathroom", 11, True, False)
beach = Room("Beach", 12, True, False)
