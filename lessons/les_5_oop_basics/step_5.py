'''

Если мы не планируем хранить какое-либо состояние, то зачем нам этот класс?
Не плоди сущности без их надобности

'''


class User:
    def __init__(self):
        self.age = None

    def get_address(self):
        pass

    def get_age(self):
        pass


class AdminUser(User):
    pass


user_1 = User()
print(vars(user_1))
user_1.age = 25
print(user_1.age)