

from dataclasses import dataclass
from Plane import Plane
from Exception import MyException

@dataclass()
class Gear(Plane):
    name: str
    wheels: int
    LANDING_GEAR_RELEASED: bool = False


    # Метод, выпускающий шасси
    def release(self):
        if self.LANDING_GEAR_RELEASED:
            raise MyException
        else:
            self.LANDING_GEAR_RELEASED = True
        return self.LANDING_GEAR_RELEASED


    # Обработка исключений
    def handling_exception(self):
        try:
            Gear.release(self)
        except MyException:
            print("Already released")
