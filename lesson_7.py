import sys
my_file = open('print.txt', 'w')


def printing(*args, sep=' ', end='\n', file=sys.stdout):
    file.write(sep.join(map(str, args)))
    file.write(end)


if __name__ == '__main__':
    printing('John', 'Bill', 'James', sep='-', file=my_file)
    printing(123456789, end=' ')
    printing('qwerty')