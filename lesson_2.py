# You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba.
# Show it in code. Keep in mind that people with the same name can be in both companies.

toshiba_personnel = ["Ann", "Mary", "Jim", "Ashley", "Garry", "James"]
eleks_personnel = ["Margo", "Andrey", "Billy", "James", "Ann"]

new_company_list = toshiba_personnel.copy()
new_company_list.extend(eleks_personnel)
print(new_company_list)

# You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
# Names of people in the format "John Dow" first and second name. Find those who are on all blacklists.

casino_blacklist = {"Han Solo", "Master Yoda", "Obi Wan Kenobi", "R2-D2", "Luke Skywalker"}
poker_blacklist = {"Graf Dooku", "Leia Organa", "Obi Wan Kenobi", "Luke Skywalker"}
alcohol_blacklist = {"Master Yoda", "Luke Skywalker", "Leia Organa", "Obi Wan Kenobi"}


total_blacklist = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(total_blacklist)

# You have two groups of people. One group consists of omnivores, the other only vegetarians.
# An omnivore is a vegetarian but a vegetarian is not an omnivore.
# Display a list of guests who can eat vegetables and herbs.

omnivore = {"James", "Sirius", "Garry"}
vegetarians = {"Luna", "Ron", "Hermione", "Petunia"}
who_can_eat_herbs = vegetarians.union(omnivore)
print(who_can_eat_herbs)

