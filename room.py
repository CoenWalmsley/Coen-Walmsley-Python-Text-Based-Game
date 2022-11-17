class Room:
    def __init__(self, name, room_number, surrounding_rooms, object_in_room=False, person_in_room=False):
        """

        :param name: The name of the room.
        :param room_number: The number of the room on the map.
        :param object_in_room: Boolean value of whether there is an object in the room or not.
        :param person_in_room: Boolean value of whether there is a person in the room or not.
        :param surrounding_rooms: The room numbers of the surrounding rooms, and the direction they are in.
        """
        self.name = name
        self.room_number = room_number
        self.object_in_room = object_in_room
        self.person_in_room = person_in_room
        self.surrounding_rooms = surrounding_rooms

    def look_around_room(self):
        if self.object_in_room is True:
            print(f"In this room, you've spotted an object, press G to grab.")
            self.object_in_room = False
        else:
            print("There are no objects in this room.")

        if self.person_in_room:
            print(f"You found someone, press T to talk to them.")
        else:
            print("There is no one else in this room.")

    def move_room(self):
        print("What rooms would you like to visit next?")
        print(self.surrounding_rooms)
