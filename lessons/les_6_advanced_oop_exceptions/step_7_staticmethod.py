import math

'''
Static methods don’t have access to cls or self. 
They work like regular functions but belong to the class’s namespace.

Static and class methods communicate and (to a certain degree) enforce 
developer intent about class design. 
This can have maintenance benefits.

@staticmethod – используется для создания метода, который ничего не знает о классе или экземпляре, 
через который он был вызван. Он просто получает переданные аргументы, без неявного первого аргумента, 
и его определение неизменяемо через наследование.

@staticmethod – это вроде обычной функции, определенной внутри класса, которая не имеет доступа к экземпляру, 
поэтому ее можно вызывать без создания экземпляра класса.

!!! Статический метод помогает в достижении инкапсуляции в классе, 
!!! поскольку он не знает о состоянии текущего экземпляра. 

Также имейте в виду, что вызов @classmethod включает в себя дополнительное выделение памяти, 
чего нет при вызове @staticmethod или обычной функции.

'''

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


if __name__ == '__main__':
    p = Pizza(4, ['mozzarella', 'tomatoes'])

    print(p.area())

    print(Pizza.circle_area(4))