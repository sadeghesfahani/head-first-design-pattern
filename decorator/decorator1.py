from abc import ABC, abstractmethod


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power = 10
        self.armor = 0
        self.equipments = ""

    def get_health(self):
        return self.health

    def get_power(self):
        return self.power

    def get_armor(self):
        return self.armor

    def get_equipments(self):
        return self.equipments


class Equipment(ABC):
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    @abstractmethod
    def get_health(self):
        pass

    @abstractmethod
    def get_power(self):
        pass

    @abstractmethod
    def get_armor(self):
        pass


class PrinceHat(Equipment):
    def __init__(self):
        super().__init__("Prince Hat", 300, 100, 5)

    def get_health(self):
        return self.health

    def get_power(self):
        return self.power

    def get_armor(self):
        return self.armor


class PrinceGloves(Equipment):
    def __init__(self):
        super().__init__("Prince Gloves", 100, 3, 1)

    def get_health(self):
        return self.health

    def get_power(self):
        return self.power

    def get_armor(self):
        return self.armor


class WearEquipment(Hero):
    def __init__(self, hero, equipment):
        super(WearEquipment, self).__init__(hero)
        self.hero = hero
        self.equipment = equipment

    def get_health(self):
        return self.hero.get_health() + self.equipment.get_health()

    def get_power(self):
        return self.hero.get_power() + self.equipment.get_power()

    def get_armor(self):
        return self.hero.get_armor() + self.equipment.get_armor()

    def get_equipments(self):
        return self.hero.get_equipments() + self.equipment.name + " "

hero = Hero("LovelyPrince")
hero = WearEquipment(hero, PrinceHat())
print(hero.get_health())
print(hero.get_power())
print(hero.get_armor())
print(hero.get_equipments())

hero = WearEquipment(hero, PrinceGloves())
print(hero.get_health())
print(hero.get_power())
print(hero.get_armor())
print(hero.get_equipments())
