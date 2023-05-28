'''

Проблема сеттеров

Мы смогли присвоить какое-то неправильное значение и всё гд-то потом нагнулось

Сеттер же разруливает данную проблему и мы ломаемся в момент установки атрибута
'''


class User:
    # def __init__(self, age, *args, **kwargs):
    def __init__(self, age):
        self.age = int(age)

    def get_address(self):
        pass

    def get_age(self):
        pass

    def set_age(self, age):
        self.age = int(age)

    def year_older(self):
        self.age += 1

class AdminUser(User):
    pass


user_1 = User('25')
print(vars(user_1))
user_1.set_age('25 years')
print(user_1.age)
user_1.year_older()
user_1.set_age('25 years')
print(user_1.age)