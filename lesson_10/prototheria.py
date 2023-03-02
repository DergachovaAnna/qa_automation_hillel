from lesson_10.mammals import Mammals
from emoji import EMOJI
import random


class Prototheria(Mammals):
    __prototheria_list = ['platypus', 'echidna', 'prochidna']
    __habitat_area = ['Australia', 'New Guinea', 'Tasmania']

    def __init__(self, name, location):
        if name.lower() in self.__prototheria_list:
            self.name = name.lower()
        else:
            self.name = None

        if location.title() in self.__habitat_area:
            self.location = location.title()
        else:
            self.location = None

        super().__init__(self.name, self.location)
        self.eggs = 0
        self.eaten_breakfast = []
        self.created = False

    @property
    def get_animal_list(self):
        return self.__prototheria_list

    @property
    def get_location_list(self):
        return self.__habitat_area

    def create_animal(self):
        """Check if the given animal species and habitat area are valid
         If valid, create the animal and set the 'created' flag to True
         Otherwise, return an error message and set the 'created' flag to False"""
        if self.name is not None and self.location is not None:
            self.created = True
            return f"Hi there, I'm a {self.name.lower()} from {self.location.title()} :D "
        else:
            self.created = False
            return f"I'm sorry, I don't recognize that animal species or habitat area is wrong."

    @property
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

    def eat(self, *foods):
        """
        Feed the animal with the given foods
        If the animal is sleeping, return an error message
        If the animal has not been created yet, return an error message
        If the food is not in the animal's menu, add it to the 'eaten_breakfast' list with a prefix 'unknown'
        """
        if self.created and not self.sleeping:
            for food in foods:
                if food in Mammals._vegan_food_menu or food in Mammals._meat_food_menu:
                    self.eaten_breakfast.append(food)
                else:
                    self.eaten_breakfast.append(f"unknown {food}")
                return f"Careful, you feed your {self.name.lower()} with some food, that is not in its menu!"
            return f"{self.name.title()} is eating {', '.join(self.eaten_breakfast)}."
        else:
            return f'Please create an animal first or wake it up!'

    def give_birth(self):
        """
        Lay eggs one by one and return the number of eggs laid
        If the animal is sleeping, return an error message
        If the animal has not been created yet, return an error message
        """
        if self.created:
            if not self.sleeping:
                self.eggs += 1
                return f'Oh, look! {self.name.title()} is laying out an egg! It is total of {self.eggs} egg(s) now..'
            else:
                return f'Ups, no way - {self.name.title()} is sleeping now.. Try to wake it up first.'
        else:
            return f'Please create an animal first or wake it up!'

    @staticmethod
    def get_picture(name: str):
        """
        Get the emoji corresponding to the given animal species name
        If the name is not found in the dictionary, return a default value
        """
        return EMOJI.get(name.lower(), 'Unknown')


if __name__ == '__main__':
    animal = Prototheria('platypus', "New Guinea")
    print(animal.create_animal())
    print(animal.give_birth())
    animal.sleep()
    print(animal.eat())
    animal.wake_up()
    print(animal.eat('Burger'))
    print(animal.eaten_breakfast)
    print(animal.move)
    animal.sleep()
    print(animal.move)
    print(animal.get_picture('boss'))


