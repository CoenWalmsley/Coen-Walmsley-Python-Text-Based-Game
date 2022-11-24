import room
from person import Person
from object import Object
from backpack import BackPack

game_map = Object("Map", room.main_entrance)
room.main_entrance.room_object_person_placement(game_map, None)
roger = Person("Roger Lynn", room.lobby, True, "Roger Lynn: I can't believe the love of my life is gone!",
               "Roger: OK OK detective, you got me!")
room.lobby.room_object_person_placement(None, roger)
knife = Object("Knife", room.bedroom_one)
room.bedroom_one.room_object_person_placement(knife, None)
comb = Object("Comb", room.ensuite)
room.ensuite.room_object_person_placement(comb, None)
napkin = Object("Napkin", room.dining)
room.dining.room_object_person_placement(napkin, None)
necklace = Object("Necklace", room.bedroom_two)
room.bedroom_two.room_object_person_placement(necklace, None)
tianna = Person("Tianna Nelson", room.living, False, "Tianna Nelson: I'm glad that cow is dead, I was sick of her "
                "taking the credit.", "Tianna: OK, I hated her, and I took her necklace, but I definitely didn't "
                                      "murder her!")
room.living.room_object_person_placement(None, tianna)
sauce = Object("Sauce", room.kitchen)
room.kitchen.room_object_person_placement(sauce, None)
suitcase = Object("Suitcase", room.butler_quarters)
maxwell = Person("Maxwell Archer", room.butler_quarters, False, "Maxwell Archer: Oh it's terrible, Becca was my "
                 "favourite client!", "Maxwell: I was planning to take a holiday before the murder happened, "
                                      "I promise!")
room.butler_quarters.room_object_person_placement(suitcase, maxwell)
shovel = Object("Shovel", room.courtyard)
room.courtyard.room_object_person_placement(shovel, None)
corkscrew = Object("Corkscrew", room.bar)
room.bar.room_object_person_placement(corkscrew, None)
razor = Object("Razor", room.bathroom)
room.bathroom.room_object_person_placement(razor, None)
ring = Object("Ring", room.beach)
room.beach.room_mapping(ring, None)


def game():
    rooms_visited = []
    current_room = room.main_entrance
    inventory = BackPack(backpack_contents=[], object_name=current_room._object.object_name)
    print("Welcome to Fatal Point, where you must solve the murder of Becca Lynn.")
    print("You arrive at the scene and walk up to the main entrance of the Lynn mansion.\n""Press L to look around,"
          "press G to collect any objects and press I to access inventory.\n""To move around, press N to go North, "
          "S to go South, W to go West and E to go East.\n""To talk to a character, press T, and to accuse a character,"
          "press A.\n""You can see the rooms you have visited by pressing R, and to quit anytime, press Q.")
    print("Once you have finished looking around, press N to go into the house.")
    while True:
        user_input = input("Enter your next move: ")
        if user_input == "L":
            current_room.look_around_room()
            continue
        elif user_input == "G":
            if current_room._object is None:
                print("There are no objects here, please try another command.")
            else:
                current_room._object.collect_object()
                inventory.add()
                current_room._object = None
                continue

        elif user_input == "I":
            inventory.list()
            continue
        elif user_input == "N":
            if current_room is not None:
                current_room.move_room(user_input)
                rooms_visited.append(current_room.name)
                current_room = current_room.north
                print(f"The surrounding rooms are {current_room.north.name} to the North, "
                      f"{current_room.south.name} to the South\n", f"{current_room.east.name} to the East, "
                      f"and {current_room.west.name} to the West.")
            else:
                print("You've entered a forbidden area, you'll be sent back to the main entrance.")
                current_room = room.main_entrance
            continue
        elif user_input == "S":
            if current_room is not None:
                current_room.move_room(user_input)
                rooms_visited.append(current_room.name)
                current_room = current_room.south
            else:
                print("You've entered a forbidden area, you'll be sent back to the main entrance.")
                current_room = room.main_entrance
            continue
        elif user_input == "E":
            if current_room is not None:
                current_room.move_room(user_input)
                rooms_visited.append(current_room.name)
                current_room = current_room.east
            else:
                print("You've entered a forbidden area, you'll be sent back to the main entrance.")
                current_room = room.main_entrance
            continue
        elif user_input == "W":
            if current_room is not None:
                current_room.move_room(user_input)
                rooms_visited.append(current_room.name)
                current_room = current_room.west
            else:
                print("You've entered a forbidden area, you'll be sent back to the main entrance.")
                current_room = room.main_entrance
            continue
        elif user_input == "T":
            if current_room.person is not None:
                current_room.person.talk_to_character()
                continue
            else:
                print("There are no people in here, please try another command.")
                continue
        elif user_input == "R":
            print(rooms_visited)
        elif user_input == "A":
            current_room.person.accuse_character()
            quit()
        elif user_input == "Q":
            print("Thanks for playing.")
            quit()

        else:
            print("Invalid move, please try again!")
            continue


if __name__ == "__main__":
    game()
