'''

Почему dataclass, а не namedtuple и обычные классы

При сравнении в dataclass сравниваются параметры, в классах иначе

В dataclass мы уже сэкономили на создании методов:
    __init__
    __str__
    __repr__
    __eq__

'''

from dataclasses import dataclass, asdict, astuple, field


@dataclass
class Point:
    x: int
    y: int


class ClassPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_point(x, y):
    return Point(x, y)


@dataclass(slots=True, kw_only=True)
class Person:
    age: int
    weight: int
    # email: Optional[str] = None
    email: str | None = None

    def increase_age(self):
        self.age += 1
        return self.age


@dataclass(frozen=True)
class Product:
    name: str
    weight: int
    price: int
    tags: list[str] = field(default_factory=list)
    # tags: list[str] = []



def main():
    p1 = get_point(10, 20)
    p2 = get_point(10, 20)
    print('p1 == p2:', p1 == p2)

    p1_class = ClassPoint(10, 20)
    p2_class = ClassPoint(10, 20)
    print('p1 == p2:', p1_class == p2_class)
    print()

    print(asdict(p1))
    print(astuple(p2))

    print(Product(1,2,3))


if __name__ == "__main__":
    main()

