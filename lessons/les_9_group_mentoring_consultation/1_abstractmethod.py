"""
АВС - абстрактный класс (интерфейс)
Всё что от него унаследовано должно уметь делать make_discount, а как
уже будут решать наследники, т.е. даём намёк, что это должно быть реализовано

АВС - это метакласс
Метаклассы - это классы, которые делают другие классы

Когда я стану топовым тим лидом и напишу базовый класс с использованием @abstractmethod ->
Я буду уверен, что всё участники команды их реализовали.
И я спокойно могу у всех потомков этого класса, юзать эти методы

"""

from abc import ABC, abstractmethod


class Product(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def make_discount(selfself, pcnt):
        pass


class NoteBook(Product):
    pass


note_1 = NoteBook('Note1', 1234)


