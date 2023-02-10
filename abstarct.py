from abc import ABC, abstractmethod


class Gadget(ABC):
    """
     Gadget class describe gadget basic characteristics
    """
    def __init__(self, weight: int, price: float):
        """
        Args:
            weight:
            price:
        """
        self.weight = weight
        self.price = price

    def turn_on(self):
        """
        Turns on the gadget
        """
        print('turn_on')

    def turn_off(self):
        """
        Turns off the gadget
        """
        print('turn_off')

    @abstractmethod
    def recharge(self):
        pass


class Tablet(Gadget):
    """
    Tablet class describe tablet basic characteristics
    """
    def __init__(self, weight: int, price: float):
        """
        Args:
            weight:
            price:
        """
        super().__init__(weight, price)

    def recharge(self):
        """
         Recharges the tablet
        """
        print("Charging")

    def __upload_of_system_components(self):
        """
        Uploads system components
        """
        print('Uploading of the system components')

    def preproduction_setup(self):
        """
        Does preproduction setup
        """
        self.__upload_of_system_components()


class Laptop(Gadget):
    """
    Laptop class describe laptop basic characteristics
    """
    def __init__(self, weight: int, price: float):
        """
        Args:
            weight:
            price:
        """
        super().__init__(weight, price)

    def recharge(self):
        """
        Recharges the laptop
        """
        print("Charging is started")

