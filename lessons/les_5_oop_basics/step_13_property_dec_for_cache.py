'''

@property используют для кэширования

Пример отложенного (lazy) вычисления:
При вызове bio второй и т.д., то мы сразу из оперативы даём значение

На заметку
В данном случае многоточие не является семантической альтернативой pass.
Если последний принято рассматривать, как индикатор намеренного отсутствия кода,
то многоточие обычно ставят в ходе разработки для корректности синтаксиса и указания на то,
что код должен быть определён в последующем — TBD (to be defined).

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




user_1 = User('Vlad', '30')

print(vars(user_1))
print(user_1.age)
print(user_1.bio)
user_1.year_older()
print(user_1.age)

# user_1.age = '25 y'
user_1.age = '25'
print(user_1.age)

