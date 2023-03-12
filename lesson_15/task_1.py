# Create an iterator that accepts a sequence and can iterate over
# value in a given range. CustomIterator(sequence, start_index, end_index)
import random
from random import sample

class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self.sequence = sequence
        self.start_index = start_index - 1
        self.end_index = end_index - 1
        self.current_index = start_index - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index < 0 or self.end_index < 0:
            raise ValueError("Please enter correct index range")

        elif self.current_index >= self.end_index:
            raise StopIteration
        sequence_value = self.sequence[self.current_index]
        self.current_index += 1
        return sequence_value


if __name__ == '__main__':
    my_list = random.sample(range(1, 30), 10)
    print(my_list)

    iterator = CustomIterator(my_list, 0, 9)

    for value in iterator:
        print(value)
