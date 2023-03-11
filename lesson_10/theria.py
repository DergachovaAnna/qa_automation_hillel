from lesson_10.mammals import Mammal
import random
from emoji import EMOJI

class Theria(Mammal):
    behaviour = {'p': 'predator', 'h': 'herbivore'}

    def __init__(self, name: str, location: str, food_habits=None):
        super().__init__(name, location)
        self.baby = 0
        self.created = False
        self.alive = False
        self.speed = random.randint(1, 100)
        if food_habits is not None:
            if food_habits in self.behaviour.keys():
                self.food_habits = food_habits
            elif food_habits in self.behaviour.values():
                self.food_habits = food_habits
            else:
                raise ValueError("Invalid food_habits value")
        else:
            self.food_habits = None

    def create_animal(self):
        self.created = True
        return self.created

    def eat(self):
        """
        Eat method to feed the animal
        """
        if self.food_habits == 'h' or self.food_habits == 'herbivore':
            if self.speed < 10:
                self.created = False
                return f'{self.name.title()} was too slow to run from predators, it was caught and eaten :(!'
            else:
                return f'{self.name.title()} would love to have some {random.choice(Mammal._vegan_food_menu)}!'
        elif self.food_habits == 'p' or self.food_habits == 'predator':
            return (
                f'{self.name.title()} can eat anything, even {random.choice(Mammal._vegan_food_menu)} '
                f'with {random.choice(Mammal._meat_food_menu)}!')
        else:
            return f'Food habits are not set, so we have no idea, ' \
                   f'what {self.name.title()} may eat..{EMOJI["dont_know"]}'

    def give_birth(self):
        if self.created and not self.sleeping:
            self.baby += 1
            return f'Such a cute baby born! The {self.name} has {self.baby} baby(s) now :)'
        else:
            return f'Ups, no way - the {self.name.lower()} is either sleeping now, or have not been created yet.. :D'


if __name__ == '__main__':
    animal = Theria('lion', 'Africa')
    animal.create_animal()
    print(animal.eat())
