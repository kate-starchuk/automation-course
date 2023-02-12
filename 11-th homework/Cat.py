class Animal:
    """
    Animal class describe animal basic characteristics
    """
    def __init__(self, name: str, size: str, energy: int):
        """
        Args:
            name: name of the animal
            size: size of the animal
            energy: energy capacity of the animal
        """
        self._name = name
        self._size = size
        self._energy = energy

    def voice(self):
        """
        Prints: placeholder for default animal voice
        """
        print('Default noise')


class Cat(Animal):
    """
    Cat class describe cat basic characteristics
    """
    def __init__(self, name: str, size: str, energy: int):
        """
        Args:
            name: name of the cat
            size: size of the cat
            energy: energy capacity of the cat
        """
        super().__init__(name, size, energy)

    def voice(self):
        """
        Distinguishes energy points from the total energy capacity when executed
        Prints: custom cat voice
        """
        self._energy = self._energy - 5
        print('Meooooooow!')

    def tygdyk(self):
        """
        Distinguishes energy points from the total energy capacity when executed
        Represents classic cat activity
        """
        self._energy = self._energy - 10

    def get_energy(self) -> int:
        """
        Returns: energy of a cat
        """
        return self._energy

    def eat(self):
        """
        Adds energy points to the total energy capacity when executed
        """
        self._energy = self._energy + 10

    def get_introduction(self) -> str:
        """
        Returns: string with information about cat size
        """
        return "I'm a " + self._size + " cat"

