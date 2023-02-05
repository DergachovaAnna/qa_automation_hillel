# Implement your own print function. It should work on all operating systems. You can't use build-in print function

import sys
my_file = open('print.txt', 'w')


def printing(*args, sep=' ', end='\n', file=sys.stdout):
    """
    Alternative print function
    :param file: if particular file is not specified, *args will be printed to console
    """
    file.write(sep.join(str(arg) for arg in args))
    file.write(end)


if __name__ == '__main__':
    printing('John', 'Bill', 'James', sep='-', file=my_file)
    printing(123456789, end=' ')
    printing('qwerty')


# Implement your realization of the function filter
sequence_1 = [1, 3, 5, 4, 3.5, 4.4, 0.1]
sequence_2 = 'ggdfdgdjjjjhgfghj'
sequence_3 = (1, 3, 5, 6, 0.9, 4.6)


def my_filter(callback, sequence):
    """
    :param callback: function with filtering condition
    :param sequence: e.g. - list, tuple, string
    :return: filtered list
    """
    result = []
    for item in sequence: # iterate through sequence of items in sequence
        if callback(item):  # apply filter function
            result.append(item)
    return result


def callback(item):
    if item:  # function require filtering statement
    # if (item % 2) == 0:
    # if 'g' in item:
        return True
    else:
        return False


print(my_filter(callback, sequence_1))
print(my_filter(callback, sequence_2))
print(my_filter(callback, sequence_3))






