class Person:
    def __init__(self, character_name, room_location, is_murderer, character_statement, character_response):
        """

        :param character_name: The name of the character.
        :param room_location: The room location of where the character is.
        :param is_murderer: Whether the character is the murderer or not.
        :param character_statement: What the character says when they are approached.
        :param character_response: What the character says when they are accused.
        """
        self.character_name = character_name
        self.room_location = room_location
        self.is_murderer = is_murderer
        self.character_statement = character_statement
        self.character_response = character_response

# Print's the character's accusation response, and whether the player has won or lost.
    def accuse_character(self):
        if self.is_murderer:
            print(self.character_response)
            print("Congratulations, you have solved the murder mystery!")
            quit()
        else:
            print(self.character_response)
            print("Incorrect, you have falsely accused!\n You have lost the game!")
            quit()

# Prints the character's statement to the console.
    def talk_to_character(self):
        if self is not None:
            print(self.character_statement)
            return
        else:
            print("No one to talk too!")
