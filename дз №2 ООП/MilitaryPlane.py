
from Plane import Plane


class MilitaryPlane(Plane):
    MAX_MISSLES = 4

    def __init__(self, *args, missles_on_wings=4, **kwargs):
        super().__init__(*args, **kwargs)
        self._missles_on_wings = missles_on_wings

        # метод, запускающий ракету
    def attack(self, missles):
        if missles > self._missles_on_wings:
            print(f"Cannot launch {missles} missles: you have only {self._missles_on_wings}")
        else: self._missles_on_wings -= missles
        print(f"You have launched {missles} missles. {self._missles_on_wings} left.")

        # метод, добавляющий ракету
    def add_missle(self, value):
        print("Adding", value, "missles")
        self._missles_on_wings += value
        if self._missles_on_wings > self.MAX_MISSLES:
            print("lost", self._missles_on_wings - self.MAX_MISSLES, "of missles")
            self._missles_on_wings = self.MAX_MISSLES
        return self._missles_on_wings
