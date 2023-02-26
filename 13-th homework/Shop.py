from abc import ABC, abstractmethod


class Item(ABC):
    """Abstract class of the item"""

    @abstractmethod
    def get_name(self) -> str:
        """Returns name of the item """
        pass


class Buckwheat(Item):
    """Represents Buckwheat item """

    def __init__(self, price: float):
        self.name = 'Гречка'
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price


class Cookie(Item):
    """Represents Cookie item"""

    def __init__(self, price: float):
        self.name = 'Печиво'
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price


class Apple(Item):
    """Represents Apple item"""

    def __init__(self, price: float):
        self.name = 'Яблуко'
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price


class Shop:
    """Represents Shop"""
    def create_item(self, item_type: str, price: float) -> Item:
        if item_type == "Гречка":
            return Buckwheat(price)
        elif item_type == "Печиво":
            return Cookie(price)
        elif item_type == "Яблуко":
            return Apple(price)
        else:
            raise ValueError("Invalid item type")



