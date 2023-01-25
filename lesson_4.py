import re

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
for name in range(len(my_list)):
    print(f"{my_list[name] : >10}")


#there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
#Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: quro}

my_string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "


result = re.findall(r'name|Amanda|age|32|salary|1500|currency|euro', my_string)
my_dict = dict(zip(result[::2], result[1::2]))
print(my_dict)







