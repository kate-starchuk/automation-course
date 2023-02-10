class Company:
    """
    Describes the basic company characteristics
    """
    def __init__(self, name: str, employees_amount: int, company_type: str):
        """
        Args:
            name:
            employees_amount:
            company_type:
        """
        self.name = name
        self.employees_amount = employees_amount
        self.company_type = company_type

    def get_name(self) -> str:
        """
        Get  name of the company
        Returns:
            self.name: company name
        """
        return self.name

    def get_company_type(self) -> str:
        """
        Get type of the company

        Returns:
            self.company_type: type of the company
        """
        return self.company_type

    def hire(self):
        """
        Adds one employee to the company
        """
        self.employees_amount = self.employees_amount + 1

    def get_employees_amount(self) -> int:
        """
        Get employees amount

        Returns:
            self.employees_amount: amount of the employees
        """
        return self.employees_amount




