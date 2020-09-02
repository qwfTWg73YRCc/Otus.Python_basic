
'''
Основной модуль: main

Базовый класс: BaseVehicle (абстрактный класс)

Наследованные от базового: Car, Plane

Наследованные от наследованных: Ferrari, MilitaryPlane

Исключение: MyException

Датаклассы: Engine, Gear (в каждом из них прописано
по одному исключению)

Демонстрация работы домашнего задания осуществляется
через главный модуль

'''

from Ferrari1 import Ferrari
from MilitaryPlane import MilitaryPlane
from Engine1 import Engine
from Gear1 import Gear



if __name__ == '__main__':
    # Примеры работы методов класса
    # Инициализация класса Ferrari

    F50 = Ferrari()
    print(f"F50.fuel {F50.fuel}")
    print(f"F50.fuel consumption {F50._fuel_consumption}")

    print('Make sound method:')

    F50.make_sound()
    print("Go method:")
    F50.go(10)
    F50.go(100)
    print('Add_fuel method:')


    F50.add_fuel(1000)
    F50.add_fuel(10000)

    # Инициализация MilitaryPlane

    Su27 = MilitaryPlane()
    print(f"Su27.fuel {Su27.fuel}")
    print(f"Su27.fuel consumption {Su27._fuel_consumption}")
    print(f"Su27.missles on wings {Su27._missles_on_wings}")
    print('go method:')

    Su27.go(10)
    Su27.go(100_000)
    print('add_fuel method:')
    Su27.add_fuel(10)
    Su27.add_fuel(100_000)
    print('attack method:')
    Su27.attack(3)
    Su27.attack(2)
    print('add_missle method:')
    Su27.add_missle(2)
    Su27.add_missle(4)

    print('Testing dataclasses:')
    print('1. Engine')
    # Engine1 = Engine1
    Engine1 = Engine(name='Internal Combustion Engine', pistons=4)
    print(Engine1)
    print(Engine1.pistons)

    print(f"Turned on: {Engine1.ENGINE_TURNED_ON}")
    Engine1.turn_on()
    print(f"Turned on: {Engine1.ENGINE_TURNED_ON}")
    print(f"Turned on: {Engine1.ENGINE_TURNED_ON}")
    print('Checking exception:')
    Engine1.handling_exception()
    print('2. Gear')
    Gear1 = Gear(name='Gears', wheels=2)
    print(Gear1)
    print(f"Gear released: {Gear1.LANDING_GEAR_RELEASED}")
    Gear1.release()
    print(f"Gear released: {Gear1.LANDING_GEAR_RELEASED}")
    print('Checking exception:')
    Gear1.handling_exception()

    print('This is the end.')
