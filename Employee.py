class Employee:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self. salary = salary

    def raise_salary(self, amount: int):
        """
        Adds amount to the salary
        Args:
            amount: sum added to salary
        """
        self.salary = self.salary + amount

    def get_salary(self):
        """
        Returns: salary of the employee
        """
        return self.salary

    def get_name(self):
        """
        Returns: name of the employee
        """
        return self.name

    def get_age(self):
        """
        Returns: age of the employee
        """
        return self.age


