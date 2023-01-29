import re

# there is a space-separated string with the names "john peter brian Morgan Adam Maria bart" convert
# the string so that each name starts with a capital letter.

my_string = "john peter brian Morgan Adam Maria bart"
print(my_string.title())

# there is a list of friends ["John", "Marta", "James", "Amanda", "Marianna"]. print to the console
# the names of each on a new line, right-aligned using the string method and formatting via f string.
# Also, above the names, in the first line, display the headings Names where the word names should
# be in the middle, and the rest of the space is filled with the symbol "*"

my_list = ["John", "Marta", "James", "Amanda", "Marianna"]
header = 'Names'

print(header.center(15, '*'))
for name in range(len(my_list)):
    print(f"{my_list[name] : >10}")


# there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ".
# Convert this string to a dictionary {name: Amanda, age: 32, salary: 1500, currency: quro}

my_string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "


result = re.findall(r'name|Amanda|age|32|salary|1500|currency|euro', my_string)
my_dict = dict(zip(result[::2], result[1::2]))
print(my_dict)


# you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"] convert it to a list of
# variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]


my_list = ["FirstItem", "FriendsList", "MyTuple"]
my_list_2 = []


for item in my_list:
    my_list_2.append(re.sub(r'(?<!^)(?=[A-Z])', '_', item).lower())

print(my_list_2)


# you have a text. break the text(attached file) into sentences. As a result, you should get a list of sentences.

text = "The Hubble.Space.Telescope (often referred to as HST or Hubble) is a space telescope that " \
       "was launched into low Earth orbit in 1990 and remains in operation.... It was not the first space telescope, " \
       "but it is one of the largest and most versatile, " \
       "renowned both as a vital research tool and as a public relations boon for astronomy. " \
       "The Hubble telescope is named after astronomer Edwin Hubble and is one of NASA's Great Observatories..... " \
       "The Space Telescope Science Institute (STScI) selects Hubble's targets and processes the resulting data, " \
       "while the Goddard Space Flight Center (GSFC) controls the spacecraft.A commission headed by Lew Allen, " \
       "director of the Jet Propulsion Laboratory, was established to determine how the error could have arisen. " \
       "The Allen Commission found that a reflective null corrector, a testing device used to achieve " \
       "a properly shaped non-spherical mirror, " \
       "had been incorrectly assembled—one lens was out of position by 1.3 mm (0.051 in)."

new_text = text.replace('.A', '. A')
list_of_sentences = new_text.split('.')

for index, text in enumerate(new_text.split('. ')):
    print(f'[{index+1}]{text}')
