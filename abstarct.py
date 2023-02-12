from abc import ABC, abstractmethod


class Gadget(ABC):
    """
     Gadget class describe gadget basic characteristics
    """
    def __init__(self, weight: int, price: float):
        """
        Args:
            weight: weight of the gadget in gr
            price: price of the gadget in usa dollars
        """
        self.weight = weight
        self.price = price

    def turn_on(self) -> str:
        """
        Turns on the gadget
        """
        return 'turn_on'

    def turn_off(self) -> str:
        """
        Turns off the gadget
        """
        return 'turn_off'

    @abstractmethod
    def recharge(self):
        pass


class Tablet(Gadget):
    """
    Tablet class describe tablet basic characteristics
    """
    def __init__(self, weight: int, price: float, screen_resolution: str):
        """
        Args:
            weight: weight of the tablet in gr
            price: price of the tablet in usa dollars
            screen_resolution
        """
        super().__init__(weight, price)
        self.screen_resolution = screen_resolution

    def recharge(self) -> str:
        """
         Recharges the tablet
        """
        return "Charging"

    def __upload_of_system_components(self) -> str:
        """
        Uploads system components
        """
        return 'Uploading of the system components'

    def preproduction_setup(self):
        """
        Does preproduction setup
        """
        self.__upload_of_system_components()


class Laptop(Gadget):
    """
    Laptop class describe laptop basic characteristics
    """
    def __init__(self, weight: int, price: float, keyboard: str):
        """
        Args:
            weight: weight of the laptop in gr
            price: price of the laptop in usa dollars
        """
        super().__init__(weight, price)
        self.keyboard = keyboard

    def recharge(self) -> str:
        """
        Recharges the laptop
        """
        return "Charging is started"

