# 2. Write a function square that takes 1 argument, the side of the square, and returns 3
# values (using a tuple): the perimeter of the square, the area of the square,
# and the diagonal of the square.

def square(square_side: int) -> tuple:
    if square_side <= 0:
        raise Exception("Sorry, no numbers below or equal to zero")
    square_perimetr = square_side * 4
    square_area = square_side * square_side
    square_diagonal = (2 ** 0.5) * square_side
    return square_perimetr, square_area, square_diagonal


print(square(1))
