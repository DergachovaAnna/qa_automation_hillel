# Describe the Train object. The class must contain fields and a method
# for adding wagons (it is necessary to add objects, instances of the wagon class). +

# Describe the class Wagon together with the train. The Wagon must contain a list of
# passengers and allow adding passengers. In the Wagon can be 10 passengers for example. ++

# When using the len function on a Wagon, I want to see the number of passengers. + When using len on a train,
# I want to see a list of Wagons without a locomotive. +

# Each wagon must have a number. +
# When printing a wagon to the console, I want to see the following "[n]" where n is the number of the wagon. +

class Train:

    def __init__(self):
        self.__list_of_wagons = ['Locomotive']
        self.__num_wagons = 1  # represents locomotive

    def add_wagon(self, wagon):
        # wagon - is an instance of Wagon class
        if not isinstance(wagon, Wagon):
            raise TypeError(f'The "wagon" should be an instance of Wagon class ')
        # prevent from adding already existing wagon number to the train
        if wagon in self.__list_of_wagons:
            raise ValueError(f'Wagon {wagon} already exists in the train')
        self.__list_of_wagons.append(wagon)
        self.__num_wagons += 1

    def __len__(self):
        return self.__num_wagons - 1

    def __str__(self):
        return f'Train has {[str(wagon) for wagon in self.__list_of_wagons[1:]]} wagons'


class Wagon:

    __wagons = []
    __passengers_in_wagon = {}

    def __init__(self, wagon_number):
        self.wagon_number = wagon_number

    @property
    def wagons(self):
        return self.__wagons

    @property
    def passengers_in_wagon(self):
        return self.__passengers_in_wagon

    def __setattr__(self, key, value):
        if key == 'wagon_number' and isinstance(value, int):
            if value in self.__wagons:
                raise ValueError(f"Wagon number {value} already exists")
            self.__wagons.append(value)
            self.__dict__[key] = value
        else:
            raise AttributeError(f"Invalid attribute {key} or value {value}")

    def add_passenger(self, name: str, wagon_number: int):
        if wagon_number not in self.__wagons:
            raise ValueError(f"Wagon number {wagon_number} does not exist")
        if len(self.__passengers_in_wagon.get(wagon_number, {})) >= 10:
            raise ValueError(f"Wagon {wagon_number} is full")
        # adds a passenger name to the wagon with number wagon_number
        # setdefault returns value of the key wagon_number if
        # it exists in the dictionary, at begginning it returns an empty list.
        return self.__passengers_in_wagon.setdefault(wagon_number, []).append(name)

    def __len__(self):
        wagon_number = self.wagon_number
        if wagon_number not in self.__wagons:
            raise ValueError(f"Wagon number {wagon_number} does not exist")
        # retrieve list of passengers in a wagon with the given wagon_number with .get(),
        # empty list is set by default to prevent error on len function
        return len(self.__passengers_in_wagon.get(wagon_number, []))

    def __str__(self):
        return f"[{self.wagon_number}]"


if __name__ == '__main__':
    wagon1 = Wagon(1)
    wagon2 = Wagon(2)
    wagon3 = Wagon(3)

    train = Train()
    train.add_wagon(wagon1)
    train.add_wagon(wagon2)
    train.add_wagon(wagon3)

    print(train)

    wagon1.add_passenger("John", 1)
    wagon1.add_passenger("Jane", 1)
    wagon1.add_passenger("Jill", 1)

    wagon2.add_passenger("Bill", 2)
    wagon2.add_passenger("Will", 2)

    print(wagon1)
    print(len(wagon1))
    print(len(train))
    print(wagon1.passengers_in_wagon)
    print(wagon1.wagons)
