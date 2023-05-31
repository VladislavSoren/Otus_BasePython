"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, cargo=0, max_cargo=10, weight=5, started=False, fuel=5, fuel_consumption=1):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, cur_cargo):
        if self.max_cargo >= cur_cargo:
            self.cargo = cur_cargo
        else:
            raise CargoOverload


if __name__ == '__main__':

    Plane_1 = Plane(cargo=0, max_cargo=10, weight=10, started=False, fuel=20, fuel_consumption=1.5)

    Plane_1.load_cargo(10)

    print(vars(Plane_1))

