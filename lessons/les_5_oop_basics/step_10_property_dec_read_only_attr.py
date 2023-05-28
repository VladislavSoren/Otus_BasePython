'''

@property - позволяемт метод использовать как атрибут
* Даёт защиту от дурака :)

Возраст юзера - read_only!!!
Это  immutable  attribute!

Надёжно как швейцарские часы.
'''


class User:
    # def __init__(self, age, *args, **kwargs):
    def __init__(self, name,  age):
        self.name = name  # mutable
        self._age = int(age)  # immutable

    @property
    def age(self):
        return self._age

    # def set_age(self, age):
    #     self._age = int(age)

    def year_older(self):
        self._age += 1


user_1 = User('Vlad', '30')

print(vars(user_1))
print(user_1.age)

user_1.age = '25 y'  # read_only!!!

