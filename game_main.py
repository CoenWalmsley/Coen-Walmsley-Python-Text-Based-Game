from room import Room
from person import Person
from object import Object

main_entrance = Room("Main Entrance", "0", {"North": "1"}, True, False)
game_map = Object("Map", main_entrance)
lobby = Room("Lobby", "1", False, True, {"North": "6", "South": "0", "East": "2", "West": "4"})
roger = Person("Roger Lynn", lobby, True, "I can't believe the love of my life is gone!",
               "OK OK detective, you got me!")
bedroom_one = Room("Bedroom One", "2", True, False, {"East": "1", "West": "3"})
knife = Object("Knife", bedroom_one)
ensuite = Room("Ensuite", "3", True, False, {"West": "2"})
comb = Object("Comb", ensuite)
dining = Room("Dining", "4", True, False, {"North": "7", "East": "1", "West": "7"})
napkin = Object("Napkin", dining)
bedroom_two = Room("Bedroom Two", "5", True, False, {"East":"4"})
necklace = Object("Necklace", bedroom_two)
living = Room("Living", "6", False, True, {"North":"10", "South": "1", "East": "9", "West": "7"})
tianna = Person("Tianna Nelson", living, False, "I'm glad that cow is dead, I was sick of her taking the limelight.",
                "OK, I hated her, and I took her necklace, but I definitely didn't murder her!")
kitchen = Room("Kitchen", "7", True, False, {"South": "4", "East": "6", "West": "8"})
sauce = Object("Sauce", kitchen)
butler_quarters = Room("Butler Quarters", "8", True, True, {"East": "7"})
suitcase = Object("Suitcase", butler_quarters)
maxwell = Person("Maxwell Archer", butler_quarters, False, "Oh it's terrible, Becca was my favourite client!",
                 "I was planning to take a holiday before the murder happened, I promise!")
courtyard = Room("Courtyard", "9", True, False, {"North": "12", "West": "6"})
shovel = Object("Shovel", courtyard)
bar = Room("Bar", "10", True, False, {"North": "11", "South": "6"})
corkscrew = Object("Corkscrew", bar)
bathroom = Room("Bathroom", "11", True, False, {"South": "10"})
razor = Object("Razor", bathroom)
beach = Room("Beach", "12", True, False, {"South": "9"})
rooms_visited = []
room_numbers = {"0": main_entrance, "1": lobby, "2": bedroom_one, "3": ensuite, "4": dining, "5": bedroom_two,
                "6": living, "7": kitchen, "8": butler_quarters, "9": courtyard, "10": bar, "11": bathroom,
                "12": beach}

current_room = main_entrance



def game():
    print("Welcome to Fatal Point, where you must solve the murder of Becca Lynn.")
    print("You arrive at the scene and walk up to the main entrance of the Lynn mansion.\n""Press L to look around.")
    user_input = input("Enter your next move: ")
    if user_input == "L":
        main_entrance.look_around_room()
    user_input = input("Enter your next move: ")
    if user_input == "G":
        game_map.collect_object()
    print("You can access your inventory ")
    user_input = input("Enter your next move: ")


if __name__ == "__game_main__":
    game()

game()