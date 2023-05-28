'''

Наследование

Увеличиваем DRY, но определённой ценой

Проблема:
Разница между классами в одну строчку и понять это оч не просто

'''


class User:
    # def __init__(self, age, *args, **kwargs):
    def __init__(self, name,  age):
        self.name = name
        self.age = age  # тут срабатывает @age.setter
        self._bio = None  # lazy

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

    # ОЧЕНЬ ЧАСТО ИСПОЛЬЗУЕТСЯ (ещё одна из причин инкапсуляции)
    @property
    def bio(self):
        if self._bio is None:
            self._bio = ...
        return self._bio

    def year_older(self):
        self._age += 1


class AdminUser:
    # def __init__(self, age, *args, **kwargs):
    def __init__(self, name,  age, access_level):
        self.name = name
        self.age = age  # тут срабатывает @age.setter
        self._bio = None  # lazy
        self.access_level = access_level

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

    # ОЧЕНЬ ЧАСТО ИСПОЛЬЗУЕТСЯ (ещё одна из причин инкапсуляции)
    @property
    def bio(self):
        if self._bio is None:
            self._bio = ...
        return self._bio

    def year_older(self):
        self._age += 1





user_1 = User('Vlad', '30')
user_2 = AdminUser('Ben', '35', 'admin')

print(vars(user_1))
print(user_1.age)
print(user_2.age)

