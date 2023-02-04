class Company:
    def __init__(self, name: str, employees_amount: int, company_type: str):
        self.name = name
        self.employees_amount = employees_amount
        self.company_type = company_type

    def get_name(self):
        """
        Returns: name of the company
        """
        return self.name

    def get_company_type(self):
        """
        Returns: type of the company
        """
        return self.company_type

    def hire(self):
        """
        Adds one employee to the company
        """
        self.employees_amount = self.employees_amount + 1

    def get_employees_amount(self):
        """
        Returns: employees amount
        """
        return self.employees_amount




