import unittest
from Room import *
from Items import *

class RoomTests(unittest.TestCase):
    """unit tester for Room class"""

    def test_building_doors(self):
        room = Room()
        room.doors = ['north', 'south', 'east', 'west']

        self.assertEqual(room.doors, ['north', 'south', 'east', 'west'])

    def test_items(self):
        room = Room()
        room.items = ['healing potion', 'vision potion']

        self.assertEqual(room.items, ['healing potion', 'vision potion'])


    def test_drawing_room(self):
        room = Room()
        room.doors = ['north', 'south', 'east', 'west']
        room.items = [HealingPotion(), VisionPotion()]

        room.__str__()

        room = Room()
        room.doors = ['north', 'east', 'west']
        room.items = [Pit()]

        room.__str__()

        room = Room()
        room.doors = ['south', 'west']
        room.items = [Exit()]

        room.__str__()

        room = Room()
        room.doors = ['south', 'north']
        room.items = [HealingPotion()]

        room.__str__()


