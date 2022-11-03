from room import Room
from living import living
from dining import dining
from butler_quarters import butler_quarters

kitchen = Room("Kitchen", True, False, None, dining, living, butler_quarters, False)
