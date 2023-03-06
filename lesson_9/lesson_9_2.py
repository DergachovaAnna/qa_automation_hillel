# Create a class with a description of the worker. Any worker, employees.
class Employee:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__position = ''
        self.__min_salary = 2000

    @property
    def position(self):
        return self.__position

    @property
    def name(self):
        return self.__name

    @property
    def min_salary(self):
        return self.__min_salary

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age: int):
        """
        Sets the age of the Employee to a new value.
        param new_age: int
        """
        max_age = 130
        if isinstance(new_age, int):
            if new_age < self.__age:
                raise ValueError(f'Sorry, but employee cant get younger. Re-check age value')
            elif self.__age <= new_age <= max_age:
                self.__age = new_age
            else:
                raise ValueError(f'Sorry, but people on Earth do not live that long yet. Re-check age value')

    def apply_for_job(self, position, min_salary):
        """
        This method takes a position, age and a min_salary parameter and checks if the salary offered is greater than
        or equal to the employee's minimum salary requirement. If it is, the employee is offered the job and their
        position and minimum salary are updated. Otherwise, employee rejects application.
        :param position: str
        :param min_salary: int, float
        """
        if 50 >= self.__age >= 20:
            if min_salary >= self.__min_salary:
                self.__position = position
                self.__min_salary = min_salary
                return f"Application accepted!"
            else:
                self.__position = '"(by default)"'
                self.__min_salary = '"(by default)"'
                return f"Sorry, the salary offered for '{position}' position is too low."
        else:
            self.__position = '"(by default)"'
            self.__min_salary = '"(by default)"'
            return f'Employees age is not eligible for job application.'

    def fire(self):
        """
        This method fires the employee by resetting their position and minimum salary to default values.
        """
        self.__position = ''
        self.__min_salary = 2000
        return f"Employee fired."

    @staticmethod
    def calculate_average_age(employee_list):
        """
        This method takes a list of employees as input and returns the average age of all employees.
        param employee_list: list
        """
        total_age = 0
        for employee in employee_list:
            total_age += employee.age
            print(employee.age)
        return total_age / len(employee_list)

    @classmethod
    def create_employee(cls, name, age, position, min_salary):
        employee = cls(name, age)
        employee.apply_for_job(position, min_salary)
        return employee

    def __str__(self):
        return f"Have created {self.name}, with age {self.age}, hired as {self.position}, with salary {self.min_salary}"


if __name__ == '__main__':
    emp_from_class1 = Employee.create_employee('Bill', 77, 'manager', 100000)
    print(emp_from_class1)

    emp_from_class2 = Employee.create_employee('Jane', 23, 'manager', 1000000)
    print(emp_from_class2)

    emp_from_inst1 = Employee('Bill', 77)
    print(emp_from_inst1.apply_for_job('manager', 100000))

    emp_from_inst2 = Employee('Jane', 23)
    print(emp_from_inst2.apply_for_job('manager', 100000))



