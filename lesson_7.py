import sys
my_file = open('print.txt', 'w')


def printing(*args, file=sys.stdout):
    file.write(str(args))


if __name__ == '__main__':
    printing('John', 'Bill', 'James', file=my_file)
    printing(123456789)
    printing('qwerty')


