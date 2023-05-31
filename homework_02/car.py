"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle


class Car(Vehicle):

    def __init__(self, engine=None, weight=5, started=False, fuel=5, fuel_consumption=1):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self):
        self.engine = 'Car'
