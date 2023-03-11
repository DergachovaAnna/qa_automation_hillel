# Describe any object of your choice in the class. I want the object to be
# printed to the console in the following format: class_name: {key: value}


class Human:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        self.alive = True
        self.employed = False
        self.salary = 0

    def __str__(self):
        _class = self.__class__.__name__
        # format attributes dict to a list to apply .join method and split data to (key: value) as one element
        list_of_attributes = [f"{key}: {value}" for key, value in self.__dict__.items()]
        # format list with elements (key: value): concatenate '/t' to each list element and then
        # apply '/n'.join that will split each element to new line without braces
        formatted_list_of_attributes = '\n'.join([f'\t {element}' for element in list_of_attributes])
        return f"{_class}: {{\n{formatted_list_of_attributes}\n\t\t}}"


if __name__ == '__main__':
    Bob = Human('Bob', 28)
    print(Bob)
