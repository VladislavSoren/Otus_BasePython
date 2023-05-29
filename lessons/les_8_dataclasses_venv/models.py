"""

pydantic в отличие от простой падсказки в виде аннотации типов реально ограничивает ввод
всякой ереси (строгие правила)

Field - нужно для динамической подстановки значение в атрибут при каждоб новом инстансе
default_factory - это объект функции, который будет генерить значение для атрибута

pydantic прикрывает нам зад когда мы в поле указываем изменяемый объект:
tags: list[str] = []

-> т.е. под капотом всё равно создаётся каждый раз новый объект списка

"""

from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    email: str | None = None


class Author(BaseModel):
    id: int
    name: str
    user: User


class Post(BaseModel):
    title: str
    body: str = ""
    created_at: datetime = Field(default_factory=datetime.utcnow)
    # tags: list[str] = Field(default_factory=list)
    tags: list[str] = []


def main():
    user = User(id="1", username="john", email='a@b.com')
    print(user)
    user_dict = user.dict()
    print(user_dict)

    author = Author(
        id=b'123',
        name='Vlad',
        user=user_dict,
    )
    print(author)
    print(repr(author))
    print(repr(author.user))
    print()

    post = Post(
        title='Python news',
        created_at="2023-05-05T10:42:42",

    )
    print(post)
    print(Post(title='new_post111', tags=['abc', b'qwe', 123]))
    print(Post(title='new_post222', tags=['abc']))

if __name__ == "__main__":
    main()