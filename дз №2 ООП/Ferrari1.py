
from Car import Car

# класс, наследованный от Car
class Ferrari(Car):
    WHEELS = 4
    MASS = 1500
    MAX_FUEL = 8000

    # super позволяет заимствовать атрибуты из метода родительского класса
    def __init__(self, *args, colour = 'green', **kwargs):
        super().__init__(*args, **kwargs)
        self.colour = colour

    def add_fuel(self, value):
        res = super().add_fuel(value)
        print("max distance now", res // self._fuel_consumption)
        print(res)
        return res

    # Метод, задающий цвет автомобиля
    def change_colour(self, user_colour):
        self.colour = user_colour
        print(f"Now your car is {user_colour}")
        return self.__colour


