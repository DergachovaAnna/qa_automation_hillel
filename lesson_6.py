# 2. Write a function square that takes 1 argument, the side of the square, and returns 3
# values (using a tuple): the perimeter of the square, the area of the square,
# and the diagonal of the square.
import re


def square_measurements(square_side: int) -> tuple:
    if square_side <= 0:
        raise Exception("Sorry, no numbers below or equal to zero can be used for the calculation")
    square_perimetr = square_side * 4
    square_area = square_side * square_side
    square_diagonal = (2 ** 0.5) * square_side
    return square_perimetr, square_area, square_diagonal


if __name__ == '__main__':
    print(square_measurements(1))

# 3. Write a function is_prime that takes 1 argument -
# a number from 2 to 1000, and returns True if it is a prime number, and False otherwise.


def is_prime(number: int) -> bool:
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for divider in range(2, number):
            if number % divider == 0:
                return False
        return True


print(is_prime(72))


# You have a file of unknown length. Write a function that will remove all numbers from each line of the file.

def remove_numbers_from_text(file):
    """
    This function will remove all numbers from each line of the file
    """
    with open(file, 'r') as file:
        result = file.read()
        result_with_no_numbers = re.sub(r'[0-9]+', '', result)
    return result_with_no_numbers


print(remove_numbers_from_text('task_1.py'))
