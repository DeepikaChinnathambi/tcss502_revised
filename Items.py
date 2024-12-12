from abc import ABC, abstractmethod
import random


class Item(ABC):
    def __init__(self, name=None, item_id=None):
        self._name = name
        self._id = item_id

    @abstractmethod
    def __str__(self):
        return self._name
    @abstractmethod
    def __repr__(self):
        return self._id


class HealingPotion(Item):
    def __init__(self, min_range=5, max_range=15):
        super().__init__()
        self._hit_points = random.randint(min_range, max_range)
        self._name = 'Healing Potion'
        self._id = 'H'

    @property
    def hit_points(self):
        return self._hit_points

    def __str__(self):
        return super().__str__()
    def __repr__(self):
        return super().__repr__()


class VisionPotion(Item):
    def __init__(self, min_range=6, max_range=10):
        super().__init__()
        self._vision_range = random.randint(min_range, max_range)
        self._name = 'Vision Potion'
        self._id = 'V'

    @property
    def vision_range(self):
        return self._vision_range

    def __str__(self):
        return super().__str__()
    def __repr__(self):
        return super().__repr__()


class Pit(Item):
    def __init__(self, min_range=-20, max_range=-5):
        super().__init__()
        self._hit_points = random.randint(min_range, max_range)
        self._name = 'Pit'
        self._id = 'X'

    @property
    def hit_points(self):
        return self._hit_points

    def __str__(self):
        return super().__str__()
    def __repr__(self):
        return super().__repr__()


class Pillar(Item):
    def __init__(self, pillar_name=None):
        super().__init__()
        if pillar_name is None:
            exit('Must Specify the Pillar Name: Abstraction, Encapsulation, Inheritance, or Polymorphism')
        self._name = str(pillar_name)
        self._id = pillar_name[0]
    def __str__(self):
        return super().__str__()
    def __repr__(self):
        return super().__repr__()


class Entrance(Item):
    def __init__(self):
        super().__init__()
        self._name = 'Entrance'
        self._id = 'i'
    def __str__(self):
        return super().__str__()
    def __repr__(self):
        return super().__repr__()


class Exit(Item):
    def __init__(self):
        super().__init__()
        self._name = 'Exit'
        self._id = 'O'
    def __str__(self):
        return super().__str__()
    def __repr__(self):
        return super().__repr__()


