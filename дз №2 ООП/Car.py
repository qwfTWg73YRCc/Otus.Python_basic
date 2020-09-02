#import math
from BaseVehicle import BaseVehicle

# класс, наследованный от базового
class Car(BaseVehicle):
    WHEELS = 4
    # MAX_FUEL = 10_000

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.__dict__.update(BaseVehicle.__dict__)


    # Метод, добавляющий горючее в бак. Если добавляется больше, чем объём бака, то выводится: "Утеряно столько-то"
    def add_fuel(self, value):
        result = super().add_fuel(value)
        print(result)
        return result
