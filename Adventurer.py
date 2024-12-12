import random
from Dequeue import *

class Adventurer:
    def __init__(self, name=None, min_range=85, max_range=100):
        self._name = name
        self._health = random.randint(min_range, max_range)
        self._healing_potions = Deque()
        self._vision_potions = Deque()
        self.pillars_found = 0
        self._pillars = []
        self.current_room = None


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def health(self):
        return self._health

    def hit_points(self, hit_points):
        self._health += hit_points

    @property
    def healing_potions(self):
        return self._healing_potions.size

    @healing_potions.setter
    def healing_potions(self, healing_potions):
        self._healing_potions.enqueue(healing_potions)

    @property
    def vision_potions(self):
        return self._vision_potions.size

    @vision_potions.setter
    def vision_potions(self, vision_potions):
        self._vision_potions.enqueue(vision_potions)

    @property
    def pillars(self):
        return self._pillars

    @pillars.setter
    def pillars(self, pillars_found):
        self._pillars.append(pillars_found)
        self.pillars_found += 1


    def take_healing_potions(self):
        if len(self._healing_potions.size)>0:
            healing = self._healing_potions.dequeue()
            self.hit_points += healing.hit_points

    def use_vision_potions(self):
        if len(self._vision_potions.size)>0:
            vision = self._healing_potions.dequeue()
            return vision.vision_range
