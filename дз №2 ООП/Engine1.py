
from Car import Car
from dataclasses import dataclass
from Exception import MyException

@dataclass()
class Engine(Car):
    name: str
    pistons: int
    ENGINE_TURNED_ON: bool = False

    # Метод, запускающий двигатель
    def turn_on(self):
        if self.ENGINE_TURNED_ON:
            raise MyException
        else:
            self.ENGINE_TURNED_ON = True
        return self.ENGINE_TURNED_ON


    # Обработка исключений
    def handling_exception(self):
        try:
            Engine.turn_on(self)
        except MyException:
            print("Already turned on")

