from abc import ABC, abstractmethod
from Items import *

class Room:
    def __init__(self, number=None, x=None, y=None, rand_gen=False):
        if number is None:
            self.number = random.randint(1, 1000)
        else:
            self.number = number
        self._items = []
        self._doors = None

        self._north = None
        self._south = None
        self._east = None
        self._west = None
        self._xcoord = x
        self._ycoord = y

        if rand_gen:
            # two True statements to help get more doors... was oddly favoring None ... ?
            self.north, self.south, self.east, self.west = random.choices([True, None], k=4)

    @property
    def xcoord(self):
        return self._xcoord
    @xcoord.setter
    def xcoord(self, value):
        self._xcoord = value

    @property
    def ycoord(self):
        return self._ycoord
    @ycoord.setter
    def ycoord(self, value):
        self._ycoord = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, values):
        self._items.append(values)

    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, values):
        """
        :param values: list of directions to place doors - north,south,east,west
        :return:
        """
        self._doors = [door.lower() for door in values]

    @property
    def north(self):
        return self._north

    @north.setter
    def north(self, value):
        self._north = value

    @property
    def south(self):
        return self._south

    @south.setter
    def south(self, value):
        self._south = value

    @property
    def east(self):
        return self._east

    @east.setter
    def east(self, value):
        self._east = value

    @property
    def west(self):
        return self._west

    @west.setter
    def west(self, value):
        self._west = value


    def pick_up_item(self, item):
        return self.items.pop(self.items.index(item))

    def display(self):
        return self.__str__()

    def draw(self):
        return self.__str__()

    def __link_rooms__(self):
        pass

    def __repr__(self):
        print(self.__str__())

    def __str__(self):
        # used deepika inspired room style, works pretty good
        string = ''

        if self._items is not None and len(self.items)==1:
            obj = self._items[0].__repr__()
        elif self._items is not None and len(self.items)>1:
            obj = 'M'
        else:
            obj = ''

        if self.north:
            string += '\n    | |    \n ***___*** '
        else:
            string += '\n           \n ********* '

        if self.east and self.west:
            string += ('\n *{:7d}* '.format(self.number) +
                       '\n=|{:^7s}|='.format(obj) +
                       '\n *       * ')

        elif self.east and not self.west:
            string += ('\n *{:7d}* '.format(self.number) +
                       '\n *{:^7s}|='.format(obj) +
                       '\n *       * ')

        elif not self.east and self.west:
            string += ('\n *{:7d}* '.format(self.number) +
                       '\n=|{:^7s}* '.format(obj) +
                       '\n *       * ')

        else:
            string += ('\n *{:7d}* '.format(self.number) +
                       '\n *{:^7s}* '.format(obj) +
                       '\n *       * ')

        if self.south:
            string += '\n ***___*** \n    | |    \n'
        else:
            string += '\n ********* \n           \n'

        # print(string)
        return string



