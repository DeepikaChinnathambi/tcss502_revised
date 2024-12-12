import numpy as np
from Items import *
from Room import *
from Dequeue import *

class Dungeon:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.room_count = 0
        self.entrance = None
        self.exit = None
        self.pillars = []
        self.grid = {}
        self._location = None

        self.__generate_rooms__()
        self.__place_items__()

    def __generate_rooms__(self):
        num_rooms = random.randint(self.min, self.max)

        for x in range(num_rooms-1,-num_rooms,-1):
            self.grid[x] = {}
            for y in range(num_rooms-1,-num_rooms,-1):
                self.grid[x][y] = None
        self.entrance = Room(number=0, x=0, y=0)
        curr = self.entrance
        self.grid[0][0] = self.entrance

        max_coord = 0
        self.room_count += 1
        queue = Deque()

        while curr:
            gen_new = True if self.room_count < num_rooms else False

            if self.entrance == curr:
                curr.north, curr.east, curr.west = True, True, True

            self.__connect_adjacent_rooms__(curr)

            try:
                if curr.north is not None and not isinstance(curr.north, Room):
                    new_room = Room(self.room_count, x=curr.xcoord, y=curr.ycoord+1, rand_gen=gen_new)
                    queue.enqueue(new_room)
                    self.grid[new_room.xcoord][new_room.ycoord] = new_room
                    curr.north, new_room.south = new_room, curr
                    self.room_count += 1
            except:
                pass

            try:
                if curr.south is not None and not isinstance(curr.south, Room):
                    new_room = Room(self.room_count, x=curr.xcoord, y=curr.ycoord-1, rand_gen=gen_new)
                    queue.enqueue(new_room)
                    self.grid[new_room.xcoord][new_room.ycoord] = new_room
                    curr.south, new_room.north = new_room, curr
                    self.room_count += 1
            except:
                pass

            try:
                if curr.east is not None and not isinstance(curr.east, Room):
                    new_room = Room(self.room_count, x=curr.xcoord+1, y=curr.ycoord, rand_gen=gen_new)
                    queue.enqueue(new_room)
                    self.grid[new_room.xcoord][new_room.ycoord] = new_room
                    curr.east, new_room.west = new_room, curr
                    self.room_count += 1
            except:
                pass

            try:
                if curr.west is not None and not isinstance(curr.west, Room):
                    new_room = Room(self.room_count, x=curr.xcoord-1, y=curr.ycoord, rand_gen=gen_new)
                    queue.enqueue(new_room)
                    self.grid[new_room.xcoord][new_room.ycoord] = new_room
                    curr.west, new_room.east = new_room, curr
                    self.room_count += 1
            except:
                pass

            curr = queue.dequeue()
            max_coord = max(abs(curr.xcoord), abs(curr.ycoord)) if curr is not None else max_coord


    def __connect_adjacent_rooms__(self, curr):
        """this algorithm finds surrounding rooms and randomly connects them or not"""
        x, y = curr.xcoord, curr.ycoord
        if curr.north and self.get_room(x, y+1) is not None and not isinstance(curr.north, Room):
            if self.__get_random_tf__():
                curr.north, self.get_room(x, y+1).south = self.get_room(x, y+1), curr
            else: curr.north = None

        if curr.south and self.get_room(x, y-1) is not None and not isinstance(curr.south, Room):
            if self.__get_random_tf__():
                curr.south, self.get_room(x, y-1).north = self.get_room(x, y-1), curr
            else: curr.south = None

        if curr.east and self.get_room(x+1, y) is not None and not isinstance(curr.east, Room):
            if self.__get_random_tf__():
                curr.east, self.get_room(x+1, y).west = self.get_room(x+1, y), curr
            else: curr.east = None

        if curr.west and self.get_room(x-1, y) is not None and not isinstance(curr.west, Room):
            if self.__get_random_tf__():
                curr.west, self.get_room(x-1, y).east = self.get_room(x-1, y), curr
            else: curr.west = None


    @staticmethod
    def __get_random_tf__():
        return random.choice([True, False])

    def get_room(self, xcoord, ycoord):
        return self.grid[xcoord][ycoord]


    # todo finish using list and strings and stuff
    def __display_map__(self, x=0, y=0, full_map=True, filename='full_map.txt'):
        """ a ton of trial and error here, just ask for map and it works... this was dense"""
        list_string = []
        string = ''
        if full_map:
            xrange = list(self.grid.keys())
            yrange = list(self.grid.keys())
            filename='full_map.txt'
        else:
            xrange = range(x-1, x+2)
            yrange = range(y-1, y+2)
            filename='local_map.txt'

        for x in xrange:
            for y in yrange:
                if self.get_room(-x, y) is not None:
                    list_string.append(self.get_room(-x,y).__str__().split('\n'))
                else:
                    list_string.append(['           ']*9)
        arr = np.array(list_string)
        fin = arr.reshape(len(xrange)*3,len(yrange)*3, order='A').transpose()
        for row in fin:
            string+='\n'
            string+=''.join(row)

        with open(filename, 'w') as f:
            f.write(string)

        # return string


    def __pick_an_exit__(self):
        """randomly pick exit"""
        while True:
            x = random.choice([i for i in self.grid.keys()])
            y = random.choice([i for i in self.grid.keys()])
            room = self.get_room(x,y)
            if room != self.entrance and room is not None:
                self.exit, room.items = room, Exit
                break


    def __place_items__(self):
        # Randomly place pillars (4 in total)
        pillars = ['Abstraction', 'Encapsulation', 'Inheritance', 'Polymorphism']
        for pillar in pillars:
            while True:
                x = random.choice([i for i in self.grid.keys()])
                y = random.choice([i for i in self.grid.keys()])
                room = self.get_room(x,y)
                if room != self.entrance and room != self.exit and not any(isinstance(item, Pillar) for item in self.pillars) and room is not None:
                    room.items = Pillar(pillar)
                    break

        for i in range(self.room_count//5):
            while True:
                x = random.choice([i for i in self.grid.keys()])
                y = random.choice([i for i in self.grid.keys()])
                room = self.get_room(x,y)
                item = random.choice([HealingPotion(), VisionPotion(), Pit(), Pit(), Pit()])
                if room != self.entrance and room != self.exit and not any(isinstance(item, Pillar) for item in room.items) and room is not None:
                    room.items = item
                    break


    def breadth_first_search_traversal(self):
        """checks if solvable"""
        queue = Deque()
        queue.enqueue(self.entrance)

        while len(queue) > 0:
            node = queue.dequeue()
            print(node.data)

            # If the room has an "Exit" item (is the exit) then it can be traversed
            if any(isinstance(item, Exit) for item in node.data.items):
                return True

            if node.north:
                queue.enqueue(node.north)
            if node.south:
                queue.enqueue(node.south)
            if node.east:
                queue.enqueue(node.east)
            if node.west:
                queue.enqueue(node.west)


    def __str__(self):
        return "\n".join(" ".join(str(room) for room in row) for row in self.rooms)
