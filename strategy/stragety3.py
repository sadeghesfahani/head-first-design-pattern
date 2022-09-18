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
    def __init__(self, name, level, range, accuracy, weather_influence_factor):
        super().__init__(name, level)
        self._range = range
        self._accuracy = accuracy
        self._weather_influence_factor = weather_influence_factor

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass
