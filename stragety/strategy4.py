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


class AttachBehavior(ABC):

    @abstractmethod
    def attack(self):
        pass


class RangeAttack(AttachBehavior):

    def __init__(self, range, accuracy, weather_influence_factor):
        self._range = range
        self._accuracy = accuracy
        self._weather_influence_factor = weather_influence_factor

    def attack(self):
        print(
            f'Attacks with a bow. Range: {self._range}, Accuracy: {self._accuracy} with the weather influence factor of {self._weather_influence_factor}')


class MelleAttack(AttachBehavior):

    def __init__(self, damage_power):
        self.damage_power = damage_power

    def attack(self):
        print(f'Attacks with a sword. damage power: {self.damage_power}')


class Archer(Character):

    def __init__(self, name, level, attack_behavior):
        super().__init__(name, level)
        self._range = range
        self.attack_behavior = attack_behavior

    def attack(self):
        self.attack_behavior.attack()

    def move(self):
        print(f'{self.name} moves slowly.')


range_behavior = RangeAttack(10, 100, 0.5)
archer = Archer('Sina', 1, range_behavior)

archer.attack()
