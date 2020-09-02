from abc import ABC, abstractmethod

# Базовый класс - средство передвижения
class BaseVehicle(ABC):
    SOUND = 'beep'
    MAX_FUEL = 10_000
    # инициализация
    @abstractmethod
    def __init__(self, fuel=5000, fuel_consumption=100):
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    @property
    def fuel(self):
        return self._fuel


    def make_sound(self):
        print(self.SOUND)

    # метод, который определяет: 1. Сколько нужно горючего;
    # 2. Хватит ли имеющегося объёма для осуществления поездки;
    # 3. Сколько останется горючего по окончанию поездки.
    def go(self, distance):
        fuel_to_spend = distance * self._fuel_consumption
        if fuel_to_spend > self.fuel:
            print(f"Cannot go, not enough fuel {self.fuel}, need {fuel_to_spend}")
            print(f"Add {fuel_to_spend - self.fuel}")
            return
        self._fuel -= fuel_to_spend
        print(f"Going {distance}, spent {fuel_to_spend}, left {self.fuel}")

    # Метод, добавляющий горючее в бак. Если добавляется больше, чем объём бака, то выводится: "Утеряно столько-то"
    def add_fuel(self, value):
        print("Adding", value, "of fuel")
        self._fuel += value
        if self._fuel > self.MAX_FUEL:
            print("lost", self._fuel - self.MAX_FUEL, "of fuel")
            self._fuel = self.MAX_FUEL
        return self._fuel