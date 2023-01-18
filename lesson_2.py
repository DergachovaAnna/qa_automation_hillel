# You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba.
# Show it in code. Keep in mind that people with the same name can be in both companies.

toshiba_personnel = ["Ann", "Mary", "Jim", "Ashley", "Garry", "James"]
eleks_personnel = ["Margo", "Andrey", "Billy", "James", "Ann"]

new_company_list = toshiba_personnel.copy()
new_company_list.extend(eleks_personnel)
print(new_company_list)
