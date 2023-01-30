# 1. Create a list of tuples with a length of 100 elements where each tuple consists of 3 elements:
# a. element is an integer that will be the left operand of the expression
# b. element is an integer that will be the right operand of the expression
# c. element is an integer from 1 to 3 where:
# identifies the addition operation
# identifies the subtraction operation
# identifies the multiplication operation

# d. You can put data into a text file with the text form or use the pickle module in binary form. If placed as text then each line should contain only elements of one tuple
# separated by spaces (eg "100 2 3"). The file must be created by a script in a pre-created \test\data directory tree.
# The directory tree must be created by the script. Push only the code to the repository (not directories or file).
import random
import os
import pickle


if __name__ == '__main__':
    left_operand = list(random.sample(range(0, 100), 100))
    right_operand = list(random.sample(range(0, 100), 100))
    random_operator = []

for i in range(0, 100):
    random_operator.append(random.randint(1, 3))

data = list(zip(left_operand, right_operand, random_operator))
print(data)


if __name__ == '__main__':

    print(os.getcwd())
    os.chdir('..')
    os.makedirs('test/data')

if __name__ == '__main__':
    print(os.getcwd())
    os.chdir('./test/data')
    print(os.getcwd())
    data_bytes = pickle.dumps(data)
    with open('data.txt', 'w+b') as file:
        result = file.write(data_bytes)

if __name__ == '__main__':
    with open('data.txt', 'rb') as file:
        final_result = pickle.load(file)
        print(final_result)
