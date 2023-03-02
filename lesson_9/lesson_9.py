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

    def calculate_location_capacity(self):
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
        if new_num_employees < 0:
            raise ValueError("Number of employees cannot be negative value")
        elif new_num_employees > AppleCompany.__MAX_EMPLOYEES_CAPACITY:
            raise ValueError(f'Exceeded max capacity of {AppleCompany.__MAX_EMPLOYEES_CAPACITY}')
        else:
            self.__num_employees = new_num_employees
            print(f'Number of employees updated to {new_num_employees}')

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
    def get_office_from_country(cls, country: str):
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
            print('Invalid production type.')
        return f'{production_type} cost is {production_cost} USD'


if __name__ == '__main__':
    office = AppleCompany('USA')
    print(office.num_employees)
    office.num_employees = -1
    print(office.num_employees)
