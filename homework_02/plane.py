"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    # Установка атрибутов класса
    cargo = 0

    # Инициализация атрибутов экземпляра класса
    def __init__(self, weight=0, fuel=5, fuel_consumption=1, max_cargo=10):
        # Вызов родительского метода __init__ для переопределения значений атрибутов создаваемого экземпляра
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        # Устанавливаем новый атрибут экземпляра класса
        self.max_cargo = max_cargo

    # Обновление cargo в случае отсутствия перегруза
    def load_cargo(self, cur_cargo):
        if self.max_cargo >= cur_cargo:
            self.cargo = cur_cargo
        else:
            raise CargoOverload

    # Обнуление cargo и возврат его последнего состояния
    def remove_all_cargo(self):
        cargo_buf = self.cargo
        self.cargo = 0
        return cargo_buf


if __name__ == '__main__':

    Plane_1 = Plane(max_cargo=10)

    Plane_1.load_cargo(10)

    print(vars(Plane_1))

