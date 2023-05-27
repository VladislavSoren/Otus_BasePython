'''

age делаем через _

Т.е. мы запрещаем ПРЯМОЙ ДОСТУП к атрибуту -> инкапсулируем его

'''


class User:
    # def __init__(self, age, *args, **kwargs):
    def __init__(self, age):
        self._age = int(age)

    def get_address(self):
        pass

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = int(age)

    def year_older(self):
        self._age += 1

class AdminUser(User):
    pass


user_1 = User('30')
print(vars(user_1))
# user_1.set_age('25 years')
print(user_1._age)
user_1.set_age('25') # теперь нам пофиг на age который пытаются присунуть)
user_1.year_older()
print(user_1.get_age())