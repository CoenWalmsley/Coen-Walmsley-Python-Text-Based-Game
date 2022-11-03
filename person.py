


class Person:
    def __init__(self, character_name, room_location, is_murderer):
        self.character_name = character_name
        self.room_location = room_location
        self.is_murderer = is_murderer

    def talk_to_character(self):
        pass

    def question_character(self):
        pass

    def accuse_character(self, is_murderer, inventory):
        if is_murderer & "Shovel" in inventory:
            print("Congratulations, you have solved the murder mystery!")
        else:
            print("Incorrect, you have falsely accused!")
