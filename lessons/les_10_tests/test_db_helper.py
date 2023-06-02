"""
!teardown!
Есть вещи которые нам нужно сделать всегда, не зависимо от того
успешно ли завершился тест или нет

Фикстуры могут быть вложенными, т.е. вызывать другие фикстуры

Pytest один раз на тест инициализирует фисктуру!

В объектно-ориентированном программировании, фиктивные объекты - это смоделированные объекты,
имитирующие поведение реальных объектов управляемыми способами,
чаще всего в рамках инициативы тестирования программного обеспечения.
Программист обычно создает фиктивный объект для проверки поведения какого-либо другого объекта,
почти так же, как конструктор автомобилей использует манекен для краш-тестов
для имитации динамического поведения человека. при ударах автомобиля.
"""

from string import ascii_letters
from random import randint, choices
from db_helper import (User,
                       get_engine,
                       get_connection,
                       Engine,
                       Connection,)

from pytest import fixture

@fixture()
def user() -> User:
    username = "".join(choices(ascii_letters, k=8))
    user = User(username=username)
    print('created user', user)
    yield user  # пример teardown
    user.delete()
    pass


@fixture()
def url_default():
    # random string
    return object()


@fixture()
def engine_default(url_default):
    # random string
    return get_engine(url=url_default)


@fixture()
def connection_default(engine_default):
    # random string
    return get_connection(engine=engine_default)


'''
На каждом тесте будут создаваться новые объекты в фикстурах, НО
в рамках одного теста это одни и те же объекты!!!
'''
def test_fixtures_connection(
        url_default,
        engine_default,
        connection_default,
):
    assert isinstance(engine_default, Engine)
    assert isinstance(connection_default, Connection)
    assert engine_default.url is url_default
    assert  connection_default.engine is engine_default



class Test_User:

    def test_set_age(self, user: User):  # Вот тут instance
        some_age = randint(1, 99)
        assert user.age != some_age
        user.set_age(some_age)
        assert user.age == some_age
        # 1/0
        # pass