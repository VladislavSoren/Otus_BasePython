"""

frozen - позволяет запретить обновление состояние (изменение атрибутов)

extra: *** полезно когда мы получает данные извне (например по API)
- ignore - мы игнорируем новые пришедшие аргументы
- allow - добавляем новые аргументы к перечню атрибутов нашего класса
- forbid - если пришли лишние аргументы, то вываливаем ошибку -> extra fields not permitted

"""


from pydantic import BaseModel, Extra
from dataclasses import dataclass


class Point(BaseModel):
    x: int
    y: int


class Person(BaseModel):
    age: int
    weight: int
    email: str = None

    def increase_age(self):
        self.age += 1
        return self.age

    class Config:
        # frozen = True
        frozen = False
        extra = Extra.ignore
        # extra = Extra.allow
        # extra = Extra.forbid




def get_point(x, y):
    return Point(x=x, y=y)


def get_person():
    return Person(age=20, weight=70, email='a@b.com', foo='bar')


def main():
    p1 = get_point(10, 20)
    print(p1)
    print(repr(p1))
    print()

    person1 = get_person()
    print(person1)
    print(repr(person1))
    print()

    person1.increase_age()
    print(person1)
    print(person1.dict())



if __name__ == "__main__":
    main()
