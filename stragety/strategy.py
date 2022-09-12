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


class Archer(Character):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self):
        print(f'{self.name} attacks with a bow.')

    def move(self):
        print(f'{self.name} moves slowly.')


class Knight(Character):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self):
        print(f'{self.name} attacks with a sword.')

    def move(self):
        print(f'{self.name} moves quickly.')


class RoyalArcher(Character):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self):
        print(f'{self.name} attacks with a bow.')

    def move(self):
        print(f'{self.name} moves slowly.')