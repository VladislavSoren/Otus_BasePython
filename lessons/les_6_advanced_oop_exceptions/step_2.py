'''

Метод - функция внутри класса

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # переопределяет метол len для объектов данного класса
    def __len__(self):
        return self.age

    # Проверка на идентичность
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False


p1 = Person('Den', 10)
p2 = Person('Sam', 12)

print(p1.name, len(p1))
print(p2.name, len(p2))