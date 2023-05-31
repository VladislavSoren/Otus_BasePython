from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    # Установка атрибутов класса
    started = False

    #  Инициализация атрибутов экземпляра класса
    def __init__(self, weight=5, fuel=5, fuel_consumption=1):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    # Проверка на наличие топлива и установка флага started
    def start(self):

        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    # Проверка достаточности топлива на преодоление переданной дистанции
    def move(self, new_weight):

        """
        Vc - расход на текущую дистанцию (л)
        W - текущая дистанция (м)
        F - расход (л/м)
        * литр и метр взяты условно

        Vc = W * F
        """

        # Обновляем значение атрибута задания дистанции на переданное значение
        self.weight = new_weight

        # Рассчитываем расход
        volume_cons = self.weight * self.fuel_consumption

        # Если нам достаточно топлива, то делаем его перерасчёт
        if self.fuel >= volume_cons:
            self.fuel -= volume_cons
        else:
            raise NotEnoughFuel






if __name__ == '__main__':

    Vehicle_1 = Vehicle(weight=10, started=False, fuel=20, fuel_consumption=1.5)

    Vehicle_1.start()

    Vehicle_1.move()

    print(vars(Vehicle_1))


