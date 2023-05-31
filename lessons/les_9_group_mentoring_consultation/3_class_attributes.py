"""
Добавляя атрибуты класса мы избавляемся от надобности передавать лишние аргументы
в инициализатор родительского класса

__repr__ - reproduction!
"""

class BaseProduct:
    PRODUCT_ALIAS = None

    def __init__(self, name, price):
        self.name = name
        self._price = price

    def make_discount(self, pcnt):
        raise NotImplementedError('should implement me!')

    def __str__(self):
        return f'{self.PRODUCT_ALIAS.title()}: {self._price}'

    # __repr__ = __str__
    def __repr__(self):
        return '''NoteBook('MacBook Pro', 1587)'''


class NoteBook(BaseProduct):
    PRODUCT_ALIAS = 'ноутбук'


# note_1 = BaseProduct('MacBook Pro', 1587)
note_1 = NoteBook('MacBook Pro', 1587)
print(note_1)
print([note_1])  # __repr__
# print(note_1.__dict__)
# print(vars(note_1))
# reper() -> NoteBook('MacBook Pro', 1587)
note_1_clone = eval(repr(note_1))
print(note_1, id(note_1))
print(note_1_clone, id(note_1_clone))

# print(note_1 == note_1)  # -> __eq__
# print(note_1 > note_1)  # -> __gt__ (greater)
# print(note_1 >= note_1)  # -> __gte__ (greater and equal)
# print(note_1 <= note_1)  # -> __lte__ (less and equal)



