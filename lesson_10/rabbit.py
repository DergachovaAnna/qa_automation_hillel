from lesson_10.theria import Theria
import random


class Rabbit(Theria):
    def __init__(self, name, location, food_habits=None):
        super().__init__(name, location, food_habits)

    def move(self):
        if self.created:
            if self.sleeping:
                return f"{self.name.title()} is sleeping and can't move right now."
            else:
                directions = ["north", "south", "east", "west"]
                distance = random.randint(1, 10)
                direction = random.choice(directions)
                return f"{self.name.title()} is jumping {distance} units {direction}. Wheee!"
        else:
            return f'Please create an animal first or wake it up!'

    def wake_up(self):
        super(Theria, self).wake_up()
        return f'{self.name.title()} wakes up..'

    def sleep(self):
        super().sleep()
        return f'Its time for {self.name.title()} to go to bed..'


if __name__ == '__main__':
    alfred = Rabbit("Alfred", "Silicon Valley")
    billy = Rabbit("Billy", "Italy")
    print(alfred.wake_up())
    print(alfred.eat())
