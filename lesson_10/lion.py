import random
from lesson_10.theria import Theria


class Lion(Theria):
    def __init__(self, name, location, food_habits=None):
        super().__init__(name, location, food_habits)
        self.hunger = 0

    def hunt(self, hunger_level: int):
        """
         Simulate lion hunting and eating its prey
        """
        self.hunger = hunger_level
        if self.food_habits not in ('h', 'herbivore'):
            if self.hunger <= 0:
                return f'{self.name.title()} is not hungry right now'
            elif self.hunger > 0:
                pray = random.choice(['zebra', 'cow', 'sheep'])
                hunger_level -= 1
                return f'{self.name.title()} has just hunted a {pray}'
        else:
            return f'{self.name.title()} is not a predator and cannot hunt for food.'


if __name__ == '__main__':
    animal = Lion('Alex', 'Africa', 'h')
    animal.create_animal()
    print(animal.hunt(0))
    print(animal.move())
