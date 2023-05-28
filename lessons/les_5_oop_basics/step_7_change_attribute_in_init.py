'''

Инициализатор - дирижер, который разруливает нормальное создание объекта (начального состояния)

'''


class User:
    # def __init__(self, age, *args, **kwargs):
    def __init__(self, age):
        self.age = int(age)

    def get_address(self):
        pass

    def get_age(self):
        pass

    def year_older(self):
        self.age += 1


# user_1 = User('25')
user_1 = User('25 year')
print(vars(user_1))
user_1.age = 25
print(user_1.age)
user_1.year_older()