# you have a list of elements [1, 2, 3, 4, 5, 6, 7, 8]. Loop through the list using the foreach loop.
# The element with an odd index is put into a new list of tuples where the first element is the
# index and the second is the value. [(index, value)]. accordingly, elements with an even index are
# placed in another list of tuples with the same format as in the case with odd indices

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
odds = []
evens = []

# for number in my_list:
#     if number % 2 == 0:
#         evens.append(number)
#     else:
#         odds.append(number)
# odds = list(enumerate(odds))
# evens = list(enumerate(evens))
# print(odds)
# print(evens)

for num in range(0, len(my_list)):
    if num % 2 == 0:
        evens.append((num, my_list[num]))
    else:
        odds.append((num, my_list[num]))
print(odds)
print(evens)
