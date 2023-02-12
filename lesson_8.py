#  Create a decorator that prints to the console the name of the function that was called.
# The function should work as intended. For example, create a pair of functions for the arithmetic
# operations of summation and multiplication. When calling these functions, the result of the
# operation must be returned and the name of the function
# that was called must be displayed in the console with the result. Small hint (__name__)

def print_name_of_function(my_function):
    def wrapper(*args, **kwargs):
        print(f'Result of function "{my_function.__name__}":')
        return my_function(*args, **kwargs)
    return wrapper


@print_name_of_function
def summation(left_operand, right_operand):
    result = left_operand + right_operand
    return result


@print_name_of_function
def multiplication(left_operand, right_operand):
    return left_operand * right_operand


if __name__ == '__main__':
    print(summation(10, 88))
    print(multiplication(4, 8))


# Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive.
# The solution should work and not freeze your computer.


def print_squares():
    """
    The function prints the squares of all even numbers between 0 and 1000000000.
    """
    def generate_squares():
        """
        The function generates the squares of all even numbers between 0 and 1000000000.
        """
        for number in range(0, 1000000001, 2):
            if number != 0:
                yield number * number
    for generated_number in generate_squares():
        print(generated_number)
    return f'Have finished the calculation'


print(print_squares())


# Find all of the numbers from 1-1000 that are divisible by 7


def divisible_by_7():
    return [number for number in range(1, 1000) if number % 7 == 0]


print(divisible_by_7())


# Find all of the numbers from 1-1000 that have a 3 in them


def numbers_with_3():
    yield [number for number in range(1, 1000) if '3' in str(number)]


print(next(numbers_with_3()))
