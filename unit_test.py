import unittest

import room
from room import Room
import game_main
from object import Object
from person import Person


class MyTestCase(unittest.TestCase):
    def test_objects(self):
        example = game_main.razor
        self.assertIsInstance(example, Object)

    def test_person(self):
        example = game_main.roger
        self.assertIsInstance(example, Person)

    def test_room(self):
        example = room.main_entrance
        self.assertIsInstance(example, Room)


if __name__ == '__main__':
    unittest.main()
