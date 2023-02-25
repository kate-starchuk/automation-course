from typing import Callable


class Action:
    """
    Class Action describes action
    """
    def __init__(self, action: Callable[[], None]):
        """
        Args:
            action: contingent action
        """
        self.__action = action

    @property
    def action(self) -> Callable[[], None]:
        """

        Returns: Callable[[], None]

        """
        return self.__action


class Human:
    """
    Class Human represents human
    """
    def __init__(self, name: str):
        """
        Args:
            name: human name
        """
        self.__name = name
        self.__action = Action(lambda: print(f'Hello from {name}'))

    @property
    def action(self) -> Callable[[], None]:
        return self.__action.action


humans = [
    Human('Ivan'),
    Human('Kate'),
    Human('Susan'),
]

for human in humans:
    human.action()



