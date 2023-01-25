# there is a space-separated string with the names "john peter brian Morgan Adam Maria bart" convert
# the string so that each name starts with a capital letter.

my_string = "john peter brian Morgan Adam Maria bart"
print(my_string.title())

#there is a list of friends ["John", "Marta", "James", "Amanda", "Marianna"]. print to the console
#the names of each on a new line, right-aligned using the string method and formatting via f string.
#Also, above the names, in the first line, display the headings Names where the word names should
#be in the middle, and the rest of the space is filled with the symbol "*"

my_list = ["John", "Marta", "James", "Amanda", "Marianna"]
header = 'Names'
print(header.center(15, '*'))
for i in range(0, len(my_list)):
    print(f"{my_list[i] : >10}")
