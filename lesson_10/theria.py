from lesson_10.mammals import Mammals


class Theria (Mammals):

    def __init__(self, name, location):
        super().__init__(name, location)

    @property
    def get_animal_list(self):
        return self.__prototheria_list

    @property
    def get_location_list(self):
        return self.__habitat_area

    def introduce_yourself(self):
        if self.name is not None and self.location is not None:
            return f"Hi there, I'm a {self.name.lower()} from {self.location.title()} :D"
        else:
            return f"I'm sorry, I don't recognize that animal species."

    def eat(self, *foods):
        for food in foods:
            if food in Mammals._vegan_food_menu or food in Mammals._meat_food_menu:
                self.eaten_breakfast.append(food)
            else:
                self.eaten_breakfast.append(f"unknown {food}")
                return f"Careful, you feed your {self.name.lower()} with some food, that is not in its menu!"
        return f"{self.name.title()} is eating {', '.join(self.eaten_breakfast)}."

    def give_birth(self):
        while not self.sleeping:
            self.eggs += 1
            return f'Oh, look! {self.name.title()} is laying out an egg! It is total of {self.eggs} egg(s) now..'
        else:
            return f'Ups, no way - {self.name.title()} is sleeping now.. Try to wake it up first.'


if __name__ == '__main__':
    animal = Prototheria('PLAtypus', "ausTralia")
    print(animal.introduce_yourself())
    print(animal.eat('worms', 'apples', 'burger'))
    print(animal.eaten_breakfast)
    print(animal.give_birth())
    print(animal.sleep())
    print(animal.move)
    print(animal.wake_up())
    print(animal.move)
