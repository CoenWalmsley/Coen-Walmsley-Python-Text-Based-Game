import room
from person import Person
from object import Object
from backpack import BackPack

game_map = Object("Map", room.main_entrance)
main_entrance = room.RoomMapping(room.lobby, None, None, None, game_map, None, room.main_entrance.name,
                                 room.main_entrance.room_number)
roger = Person("Roger Lynn", room.lobby, True, "I can't believe the love of my life is gone!",
               "OK OK detective, you got me!")
lobby = room.RoomMapping(room.living, room.main_entrance, room.bedroom_one, room.dining, None, roger, room.lobby.name,
                         room.lobby.room_number)
knife = Object("Knife", room.bedroom_one)
bedroom_one = room.RoomMapping(None, None, room.ensuite, room.lobby, knife, None, room.bedroom_one.name,
                               room.bedroom_one.room_number)
comb = Object("Comb", room.ensuite)
ensuite = room.RoomMapping(None, None, None, room.bedroom_one, comb, None, room.ensuite.name, room.ensuite.room_number)
napkin = Object("Napkin", room.dining)
dining = room.RoomMapping(room.kitchen, None, room.lobby, room.bedroom_two, napkin, None, room.dining.name,
                          room.dining.room_number)
necklace = Object("Necklace", room.bedroom_two)
bedroom_two = room.RoomMapping(None, None, room.dining, None, necklace, None, room.bedroom_two.name,
                               room.bedroom_two.room_number)
tianna = Person("Tianna Nelson", room.living, False, "I'm glad that cow is dead, I was sick of her taking the limelight.",
                "OK, I hated her, and I took her necklace, but I definitely didn't murder her!")
living = room.RoomMapping(room.bar, room.lobby, room.courtyard, room.kitchen, None, tianna, room.living.name,
                          room.living.room_number)
sauce = Object("Sauce", room.kitchen)
kitchen = room.RoomMapping(None, room.dining, room.living, room.butler_quarters, sauce, None, room.kitchen.name,
                           room.kitchen.room_number)
suitcase = Object("Suitcase", room.butler_quarters)
maxwell = Person("Maxwell Archer", room.butler_quarters, False, "Oh it's terrible, Becca was my favourite client!",
                 "I was planning to take a holiday before the murder happened, I promise!")
butler_quarters = room.RoomMapping(None, None, room.kitchen, None, suitcase, maxwell, room.butler_quarters.name,
                                   room.butler_quarters.room_number)
shovel = Object("Shovel", room.courtyard)
courtyard = room.RoomMapping(room.beach, None, None, room.living, shovel, None, room.courtyard.name,
                             room.courtyard.room_number)
corkscrew = Object("Corkscrew", room.bar)
bar = room.RoomMapping(room.bathroom, room.living, None, None, corkscrew, None, room.bar.name, room.bar.room_number)
razor = Object("Razor", room.bathroom)
bathroom = room.RoomMapping(None, room.bar, None, None, razor, None, room.bathroom.name, room.bathroom.room_number)
ring = Object("Ring", room.beach)
beach = room.RoomMapping(None, room.courtyard, None, None, ring, None, room.beach.name, room.beach.room_number)

inventory = BackPack(None)
current_room = main_entrance


def game():
    print("Welcome to Fatal Point, where you must solve the murder of Becca Lynn.")
    print("You arrive at the scene and walk up to the main entrance of the Lynn mansion.\n""Press L to look around,"
          "press G to collect any objects and press I to access inventory.\n""To move around, press N to go North, "
          "S to go South, W to go West and E to go East.\n""To talk to a character, press T, and to accuse a character,"
          "press H.")
    user_input = input("Enter your next move: ")
    if user_input == "L":
        current_room.look_around_room()
    elif user_input == "G":
        current_room.object.collect_object()
    elif user_input == "I":
        inventory.in_backpack()
    elif user_input == "N" or "S" or "W" or "E":
        current_room.move_room()
    elif user_input == "T":
        current_room.person.talk_to_character()
    elif user_input == "A":
        current_room.person.accuse_character()
    elif user_input == "Q":
        quit()


if __name__ == "__game_main__":
    game()

game()
