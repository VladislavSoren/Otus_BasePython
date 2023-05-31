from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):

    #  Инициализация атрибутов класса
    def __init__(self, weight=5, started=False, fuel=5, fuel_consumption=1):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    #
    def start(self):

        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    #
    def move(self):

        """
        Vc - расход на текущую дистанцию (л)
        W - текущая дистанция (м)
        F - расход (л/м)
        * литр и метр взяты условно

        Vc = W * F
        """

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


