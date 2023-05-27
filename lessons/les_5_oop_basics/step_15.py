'''

Решение - Наследование

Мы переиспользуем код класса предка

Полиморфизм
Мы одинаково со всеми объектами работаем (общие свойства)

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


class AdminUser(User):
    MAX_AGE = 60

    def __init__(self, name,  age, access_level):
        super().__init__(name,  age)  # то что есть у родителя
        self.access_level = access_level  # что-то новенькое

    # Расширение метода родителя
    def year_older(self):
        super().year_older()
        if self._age > self.MAX_AGE:
            raise Exception('too old admin')



user_1 = User('Vlad', '30')
user_2 = AdminUser('Ben', '35', 'admin')
print(user_1.age)
print(user_2.age)

# Пример полиморфизма
users = [user_1, user_2]
for user in users:
    print(user.age)
