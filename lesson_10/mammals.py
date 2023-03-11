from abc import ABC, abstractmethod
import random
from emoji import EMOJI


class Mammal(ABC):
    _vegan_food_menu = ['grass', 'apples', 'bananas', 'kivi', 'blueberry', 'strawberry', 'tomato', 'cucumber']
    _meat_food_menu = ['beef', 'zebra', 'insects', 'worms']

    def __init__(self, name: str, location: str = None):
        self.name = name
        self.location = location
        self.sleeping = False
        self.waking_up = True
        self.created = False

    def sleep(self):
        """ Set animal to sleep changing flag state """
        self.sleeping = True
        self.waking_up = False
        return f'z-z-z-z-z..'

    def wake_up(self):
        """ Set animal to awake changing the flag state """
        self.waking_up = True
        self.sleeping = False
        return f'Good morning!'

    def move(self):
        """
         Move the animal in a random direction with a random distance
         If the animal is sleeping, return an error message
         If the animal has not been created yet, return an error message
        """
        if self.created:
            if self.sleeping:
                return f"{self.name.title()} is sleeping and can't move right now."
            else:
                directions = ["north", "south", "east", "west"]
                distance = random.randint(1, 10)
                direction = random.choice(directions)
                return f"{self.name.title()} is moving {distance} units {direction}."
        else:
            return f'Please create an animal first or wake it up!'

    @abstractmethod
    def create_animal(self):
        pass

    @abstractmethod
    def give_birth(self):
        pass

    @staticmethod
    def get_picture(name: str):
        """
        Get the emoji corresponding to the given animal species name
        If the name is not found in the dictionary, return a default value
        """
        return EMOJI.get(name.lower(), 'Unknown')
