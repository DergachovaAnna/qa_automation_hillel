# Create an iterator that accepts a sequence and can iterate over
# value in a given range. CustomIterator(sequence, start_index, end_index)
import random


class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index - 1
        self.__end_index = end_index - 1
        self.__current_index = start_index - 1

        if self.__start_index < 0 or self.__end_index < 0:
            raise ValueError("Please enter correct index range")

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index >= self.__end_index:
            raise StopIteration
        sequence_value = self.__sequence[self.__current_index]
        self.__current_index += 1
        return sequence_value


if __name__ == '__main__':
    my_list = random.sample(range(1, 30), 10)
    print(my_list)

    iterator = CustomIterator(my_list, 5, 9)

    for value in iterator:
        print(value)
