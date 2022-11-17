from object import Object
class Person:
    def __init__(self, character_name, room_location, is_murderer, character_statement, character_response):
        self.character_name = character_name
        self.room_location = room_location
        self.is_murderer = is_murderer
        self.character_statement = character_statement
        self.character_response = character_response

    def accuse_character(self):
        if self.is_murderer & "Ring" in Object.inventory:
            print(self.character_response)
            print("Congratulations, you have solved the murder mystery!")
            quit()
        else:
            print(self.character_response)
            print("Incorrect, you have falsely accused!\n You have lost the game!")
            quit()

    def talk_to_character(self):
        print(self.character_statement)
        return
