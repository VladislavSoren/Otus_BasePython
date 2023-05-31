"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle


class Car(Vehicle):

    # Установка атрибутов класса
    engine = None

    # Инициализация атрибутов экземпляра класса
    def __init__(self, weight=5, fuel=5, fuel_consumption=1):
        # Вызов родительского метода __init__ для переопределения значений атрибутов создаваемого экземпляра
        super().__init__(weight, fuel, fuel_consumption)

    # Устанавливает тип движка
    def set_engine(self, engine_type):
        self.engine = engine_type
