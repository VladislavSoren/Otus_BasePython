'''

@age.setter срабатывает в момент инициализации
* Надёжно
* Избавляемся от дублирования

'''


class User:
    # def __init__(self, age, *args, **kwargs):
    def __init__(self, name,  age):
        self.name = name
        self.age = age  # тут срабатывает @age.setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age_setter(age)

    def _age_setter(self, age):
        self._age = int(age)
        ...
        ...

    def year_older(self):
        self._age += 1


user_1 = User('Vlad', '30')

print(vars(user_1))
print(user_1.age)
user_1.year_older()
print(user_1.age)

# user_1.age = '25 y'
user_1.age = '25'
print(user_1.age)

