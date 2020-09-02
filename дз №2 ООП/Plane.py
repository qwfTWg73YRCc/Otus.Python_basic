

from BaseVehicle import BaseVehicle


# класс, наследованный от базового
class Plane(BaseVehicle):
    WHEELS = 4
    MAX_FUEL = 10_000_000
    MAX_HEIGHT = 11_000

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def fly(self, height):
        if height > self.MAX_HEIGHT:
            print(f"Cannot fly: {height} is more than maximum height: {self.MAX_HEIGHT}")


    def add_fuel(self, value):
        super().add_fuel(value)

