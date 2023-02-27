# Create a class describing any company. For example, Toshiba or Apple
class AppleCompany:
    # A private class attribute that stores the maximum number of employees allowed for the company.
    __MAX_EMPLOYEES_CAPACITY = 1000

    # A private class attribute that stores dict of company offices locations.
    __offices_locations = {
        'USA': 'New York',
        'China': 'Shanghai',
        'Japan': 'Tokyo',
        'Ukraine': 'Kharkiv'
    }

    def __init__(self, location: str):
        """
        Constructor for AppleCompany class.
        Args: - location (str): The location (country) of the company is an instance attribute.
        Should be a value from offices_locations dict.
        """
        self.__location = location
        self.__num_employees = 0

    def location_capacity(self):
        """This method calculates the number of vacant positions left in the company's location."""
        left_capacity = AppleCompany.__MAX_EMPLOYEES_CAPACITY - self.__num_employees
        if self.__location in AppleCompany.__offices_locations.keys():
            return f'{left_capacity} vacant positions left in {self.__location}'
        else:
            raise ValueError(f'Invalid location. Check that created instances location is from offices_locations dict')

    @property
    def num_employees(self):
        """Getter method for the private attribute __num_employees."""
        return f'{self.__num_employees} employees are currently hired'

    @num_employees.setter
    def num_employees(self, new_num_employees):
        """
        Setter method for the private attribute __num_employees.
        Args: - new_num_employees (int): The new number of employees.
        Raises: - ValueError: If the new number of employees exceeds the maximum capacity allowed for the company.
        """
        if new_num_employees <= AppleCompany.__MAX_EMPLOYEES_CAPACITY:
            self.__num_employees = new_num_employees
            print(f'Number of employees updated to {new_num_employees}')
        else:
            raise ValueError(f'Exceeded max capacity of {AppleCompany.__MAX_EMPLOYEES_CAPACITY}')

    @property
    def company_location(self):
        """Getter method for the private attribute __location."""
        return self.__location

    def get_profit_by_location(self, revenue: int, expenses: int):
        """
        Calculate the profit in the company's location.
        Args: - revenue (int): The revenue of the company.
              - expenses (int): The expenses of the company.
        """
        profit = revenue - expenses
        print(f'Profit in {self.__location} is {profit} USD')

    @classmethod
    def from_country(cls, country: str):
        """
        Class method to create an instance of AppleCompany based on the country.
        Args: - country (str): The country to get location of the company, taking result by key's value
        from offices_locations dictionary
        Returns: An instance of the AppleCompany class.
        """
        location = AppleCompany.__offices_locations.get(country, 'Unknown')  # 'Unknown' - default value
        return cls(location)

    @staticmethod
    def get_production_cost(production_type: str):
        """
        Static method to get the production cost of a specific Apple product.
        Args: - production_type (str): The type of Apple product to get the production cost for.
        Returns:- str: A string that displays the production cost for the given product type.
        """
        production_cost = 0
        if production_type == 'iPhone':
            production_cost = 500
        elif production_type == 'iPad':
            production_cost = 350
        elif production_type == 'MacBook':
            production_cost = 1000
        else:
            print('Invalid production type')
        return f'{production_type} cost is {production_cost} USD'


# Create a class with a description of the worker. Any worker, employees.
class Employees:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__position = ''
        self.__min_salary = 2000

    @property
    def position(self):
        return self.__position

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
        if isinstance(new_age, int):
            if new_age < self.__age:
                raise ValueError(f'Sorry, but employee cant get younger. Re-check age value')
            elif new_age >= self.__age:
                self.__age = new_age

    def employee_apply_for_job(self, position, min_salary):
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
                return f"Sorry, the salary offered for '{position}' position is too low."
        else:
            return f'Employees age is not eligible for job application'

    def employee_fire(self):
        """
        This method fires the employee by resetting their position and minimum salary to default values.
        """
        self.__position = ''
        self.__min_salary = 2000
        return f"Employee fired."

    @classmethod
    def average_age(cls, employee_list):
        """
        This method takes a list of employees as input and returns the average age of all employees.
        param employee_list: list
        """
        total_age = 0
        for employee in employee_list:
            total_age += employee.age
            print(employee.age)
        return total_age / len(employee_list)


if __name__ == '__main__':
    # office_1 = AppleCompany.from_country('USA')
    # print(office_1.company_location)
    # print(office_1.location_capacity())

    emp1 = Employees('Bob', 38)
    # print(emp1.age)
    # emp1.set_new_age = 55
    # print(emp1.age)
    # emp1.set_new_age = 51
    # print(emp1.age)

    emp2 = Employees('Bill', 30)
    emp_list = [emp1, emp2]
    average_age = Employees.average_age(emp_list)
    print(average_age)
