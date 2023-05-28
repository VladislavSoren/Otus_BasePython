'''

# isinstance = экземпляр

# double underscore
# underscore = "_"
# double underscore -> d_under
# double underscore -> dunder

dunder методы уже есть в дефолтном классе object (батя всех классов)
Мы перееинициализируем существующие dunder методы класса python, изменяя их под свои нужды

Методы:
    __str__
    __repr__

'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Краткая информация о содержимом объекта
    def __str__(self):
        return f'x={self.x} y={self.y}'

    # Подробное описалово объекта
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    # Проверка на идентичность (переопределили "==")
    def __eq__(self, other):
        # isinstance = экземпляр
        if not isinstance(other, self.__class__):
            return False

        return (self.x == other.x) and (self.y == other.y)

    def add(self, point):
        return self.__class__(x=self.x + point.x, y=self.y + point.y)  # аналогично Point(...), только гибко

    # Переопределяем работу с дандер методом оператора "+"
    def __add__(self, other):
        return self.add(other)

    # Переопределяем работу с дандер методом оператора "+="
    def __iadd__(self, other):
        # in-place add

        self.x += other.x
        self.y += other.y

        return self

if __name__ == '__main__':
    print('Общая информация о классе Point: ', Point.mro())

    # Инстансы (объявления объектов класса)
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(5, 6)
    print('')

    # Выводим информацию о содержимом каждого объекта (__str__)
    print('Результат работы __str__')
    print(p1)
    print(p2)
    print(p3)
    print()

    # Проверка на идентичность str и __str__ (мы его переопределили в классе)
    assert str(p1) == p1.__str__()


    # Выводим подробное описание объекта (__repr__)
    print('Результат работы __repr__')
    a, b, c = 12, '12', 12.12
    items = [a, b, c]
    print(b)
    print(repr(b))
    print(items)
    print(repr(items))
    print()

    print('Результат работы __repr__ для объектов класса')
    print(repr(p1))
    print(repr(p2))
    print(repr(p3))
    print()

    print('Результат работы __eq__ для объектов класса')
    print('p1 == p2', p1 == p2)
    print('p2 == p3', p2 == p3)
    print('p1 == p3', p1 == p3)
    p4 = p1
    print('p4 == p1', p4 == p1)
    print()

    print('Проверка на тождественность (что они ссылаются на один объект)')
    print('p1 is p2', p1 is p2)
    print('p2 is p3', p2 is p3)
    print('p1 is p3', p1 is p3)
    print('p4 is p1', p4 is p1)
    print()

    print('Получение нового объекта через метод сложения "add"')
    p5 = p3.add(p4)
    p6 = p3 + p4
    print(p3, p4)
    print('p5 representation: ', repr(p5))
    print('p6 representation: ', repr(p6))
    print()

    print('Получение нового объекта через метод сложения "iadd"')
    print(p1, p2)
    p1 += p2
    print(p1)
    print()
    print()

