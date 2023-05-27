'''

Инстанцирование (instance) - передача атрибутов состояния при создании класса
Задача инициализатора - создать начальное состояние объекта, валидное для дальнейшей работы с ним

Избегайте конфликтов атрибутов с вызовом методов
'''


class User:
    # def __init__(self, age, *args, **kwargs):
    def __init__(self, age):
        self.age = age

    def get_address(self):
        pass

    def get_age(self):
        pass

    def year_older(self):
        self.age += 1

class AdminUser(User):
    pass


user_1 = User(20, name='Ivan')
print(vars(user_1))
user_1.age = 25
print(user_1.age)
user_1.year_older()