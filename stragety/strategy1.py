from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, level, range=None, accuracy=None):
        self.name = name
        self.level = level
        self._range = range
        self._accuracy = accuracy

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Archer(Character):
    def __init__(self, name, level, range, accuracy):
        super().__init__(name, level, range, accuracy)

    def attack(self):
        print(f'{self.name} attacks with a bow. Range: {self._range}, Accuracy: {self._accuracy}')

    def move(self):
        print(f'{self.name} moves slowly.')


class RoyalArcher(Character):
    def __init__(self, name, level, range, accuracy):
        super().__init__(name, level, range, accuracy)

    def attack(self):
        print(f'{self.name} attacks with a bow. Range: {self._range}, Accuracy: {self._accuracy}')

    def move(self):
        print(f'{self.name} moves slowly.')