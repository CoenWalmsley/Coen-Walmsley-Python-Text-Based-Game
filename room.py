class Room:
    def __init__(self, name, room_number, _object=None, person=None, north=None, south=None, east=None, west=None):
        """

        :param name: The name of the room.
        :param room_number: The number of the room.
        :param _object: Refers to the object instance that is inside the room.
        :param person: Refers to the person instance that is inside the room.
        :param north: Travels to the closest North room.
        :param south: Travels to the closest South room.
        :param east: Travels to the closest East room.
        :param west: Travels to the closest West room.
        """
        self.name = name
        self.room_number = room_number
        self._object = _object
        self.person = person
        self.north = north
        self.south = south
        self.east = east
        self.west = west

# Allows the user to look around the room to find the object and/or person.
    def look_around_room(self):
        if self._object is not None:
            if self.person is None:
                print("In this room, you've spotted an object, press G to grab.")
                print("In this room, there are no people.")
            else:
                print("In this room, you've spotted an object, press G to grab.")
                print("You found someone, press T to talk to them.")

        elif self._object is None:
            if self.person is not None:
                print("You found someone, press T to talk to them.")
                print("In this room, there are no objects.")
            else:
                print("In this room, there are no objects or people.")

# Adds the closest rooms by direction to the room instances.
    def room_mapping(self, north_room=None, south_room=None, east_room=None, west_room=None):
        """

        :param north_room: The room closest to the North of the current room.
        :param south_room: The room closest to the South of the current room.
        :param east_room: The room closest to the east of the current room.
        :param west_room: The room closest to the west of the current room.
        """
        self.north = north_room
        self.south = south_room
        self.east = east_room
        self.west = west_room

# Shows the player what rooms are around the current room they are in when they move.
    def show_surrounding_rooms(self):
        if self.north is None:
            print("You cannot travel North from this room.")
        else:
            print(f"You can travel North to the {self.north.name}.")
        if self.south is None:
            print("You cannot travel South from this room.")
        else:
            print(f"You can travel South to the {self.south.name}.")
        if self.east is None:
            print("You cannot travel East from this room.")
        else:
            print(f"You can travel East to the {self.east.name}.")
        if self.west is None:
            print("You cannot travel West from this room.")
        else:
            print(f"You can travel West to the {self.west.name}.")

    def room_object_person_placement(self, _object, person):
        """

        :param _object: Places the object in the room.
        :param person: PLaces the person in the room.
        """
        self._object = _object
        self.person = person

    def move_room(self, user_input):
        """

        :param user_input: The keyboard input of the player.
        :return:
        """
        if user_input == "N":
            if self.north is not None:
                print(f"You are now in {self.north.name}.")
            else:
                print("No room found, please travel another direction.")
        elif user_input == "S":
            if self.south is not None:
                print(f"You are now in {self.south.name}.")
            else:
                print("No room found, please travel another direction.")
        elif user_input == "E":
            if self.east is not None:
                print(f"You are now in {self.east.name}.")
            else:
                print("No room found, please travel another direction.")
        elif user_input == "W":
            if self.west is not None:
                print(f"You are now in {self.west.name}.")
            else:
                print("No room found, please travel another direction.")

# The initialisation of the room instances.


main_entrance = Room("Main Entrance", 0, True, False)
lobby = Room("Lobby", 1, False, True)
bedroom_one = Room("Bedroom One", 2, True, False)
ensuite = Room("Ensuite", 3, True, False)
dining = Room("Dining Room", 4, True, False)
bedroom_two = Room("Bedroom Two", 5, True, False)
living = Room("Living Room", 6, False, True)
kitchen = Room("Kitchen", 7, True, False)
butler_quarters = Room("Butler Quarters", 8, True, True)
courtyard = Room("Courtyard", 9, True, False)
bar = Room("Bar", 10, True, False)
bathroom = Room("Bathroom", 11, True, False)
beach = Room("Beach", 12, True, False)

# Adds to the instances the closest rooms by direction.


main_entrance.room_mapping(lobby, None, None, None)
lobby.room_mapping(living, main_entrance, bedroom_one, dining)
bedroom_one.room_mapping(None, None, ensuite, lobby)
ensuite.room_mapping(None, None, None, bedroom_one)
dining.room_mapping(kitchen, None, lobby, bedroom_two)
bedroom_two.room_mapping(None, None, dining, None)
living.room_mapping(bar, lobby, courtyard, kitchen)
kitchen.room_mapping(None, dining, living, butler_quarters)
butler_quarters.room_mapping(None, None, kitchen, None)
courtyard.room_mapping(beach, None, None, living)
bar.room_mapping(bathroom, living, None, None)
bathroom.room_mapping(None, bar, None, None)
beach.room_mapping(None, courtyard, None, None)
