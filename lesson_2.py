# TASK 2: You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba.
# Show it in code. Keep in mind that people with the same name can be in both companies.

toshiba_personnel = ["Ann", "Mary", "Jim", "Ashley", "Garry", "James"]
eleks_personnel = ["Margo", "Andrey", "Billy", "James", "Ann"]

toshiba_personnel.extend(eleks_personnel)
eleks_personnel.clear()
print(toshiba_personnel)
print(eleks_personnel)

# TASK 3: You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
# Names of people in the format "John Dow" first and second name. Find those who are on all blacklists.

casino_blacklist = {"Han Solo", "Master Yoda", "Obi Wan Kenobi", "R2-D2", "Luke Skywalker"}
poker_blacklist = {"Graf Dooku", "Leia Organa", "Obi Wan Kenobi", "Luke Skywalker"}
alcohol_blacklist = {"Master Yoda", "Luke Skywalker", "Leia Organa", "Obi Wan Kenobi"}

total_blacklist = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(total_blacklist)

# TASK 4: You have two groups of people. One group consists of omnivores, the other only vegetarians.
# An omnivore is a vegetarian but a vegetarian is not an omnivore.
# Display a list of guests who can eat vegetables and herbs.

omnivores = {"James", "Sirius", "Garry"}
vegetarians = {"Luna", "Ron", "Hermione", "Petunia"}
who_can_eat_herbs = vegetarians.union(omnivores)
print(who_can_eat_herbs)

# TASK 5: You have a group of guests for the VIP box. The seats in the VIP box are all occupied by these guests.
# There is a group of guests in the common room and there are still places in it.
# Display 2 groups of guests in code.


my_seats = {
    "vip_seats": {1: "occupied", 2: "occupied", 3: "occupied", 4: "occupied"},
    "common_seats": {1: "occupied", 2: None, 3: None, 4: None}
}

# TASK 6: You have a group of people with non-unique names.
# Generate a list of non-duplicate names (you cannot use set for this task).
# If there are 2 johns in the list, you need to take only one of them.
# "John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow "

mixed_list = ["Maggy Smith", "John Doe", "John Doe", "Jane Smith", "Maggy Smith", "Bill Johns", "Amely Doe"]

# for name in mixed_list:
#     if name in unique_list:
#         continue
#     else:
#         unique_list.append(name)
# print(unique_list)

unique_list = list(dict.fromkeys(mixed_list))
print(unique_list)
