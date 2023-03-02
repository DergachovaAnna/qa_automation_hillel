from abc import ABC, abstractmethod
import random


class Mammals(ABC):
    _vegan_food_menu = ['grass', 'apples', 'bananas', 'kivi', 'blueberry', 'strawberry', 'tomato', 'cucumber']
    _meat_food_menu = ['beef', 'zebra', 'insects', 'worms']

    def __init__(self, name: str, location: str = None):
        self.name = name
        self.location = location
        self.sleeping = False
        self.waking_up = True

    def sleep(self):
        self.sleeping = True
        self.waking_up = False
        return f'z-z-z-z-z..'

    def wake_up(self):
        self.waking_up = True
        self.sleeping = False
        return f'Good morning!'

    def move(self):
        if self.sleeping:
            return f"{self.name.title()} is sleeping and can't move right now."
        else:
            directions = ["north", "south", "east", "west"]
            distance = random.randint(1, 10)
            direction = random.choice(directions)
            return f"{self.name.title()} is moving {distance} units {direction}."

    @abstractmethod
    def create_animal(self):
        pass

    @abstractmethod
    def eat(self, food: str):
        pass

    @abstractmethod
    def give_birth(self):
        pass
