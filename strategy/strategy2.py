from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, level):
        self.name = name
        self.level = level

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass


class RangeCharacter(ABC, Character):
    def __init__(self, name, level, range, accuracy):
        super().__init__(name, level)
        self._range = range
        self._accuracy = accuracy

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass


class MelleCharacter(ABC, Character):
    def __init__(self, name, level, speed):
        super().__init__(name, level)
        self._speed = speed

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Archer(RangeCharacter):
    def __init__(self, name, level, range, accuracy):
        super().__init__(name, level, range, accuracy)

    def attack(self):
        print(f'{self.name} attacks with a bow. Range: {self._range}, Accuracy: {self._accuracy}')

    def move(self):
        print(f'{self.name} moves slowly.')


class Knight(MelleCharacter):
    def __init__(self, name, level, speed):
        super().__init__(name, level, speed)

    def attack(self):
        print(f'{self.name} attacks with a sword.')

    def move(self):
        print(f'{self.name} moves quickly.')
