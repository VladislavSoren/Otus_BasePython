"""
СЛОЙ ВЗАИМОДЕЙСТВИЯ С ДАННЫМИ

CRUD (Create Read Update Delete)

Модуль с функциями выполнения запрошенных действий

"""

from pydantic import BaseModel

from .schemas import User, UserIn


class Storage(BaseModel):
    users: dict[int, User] = {}  # на базе изменяемых объектов можно только в pydantic
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create_user(self, username: str):
        user = User(
            id=self.next_id,
            username=username,
        )
        self.users[user.id] = user
        return user


storage = Storage()


def get_users() -> list[User]:
    return list(storage.users.values())


def create_user(user_in: UserIn) -> User:
    return storage.create_user(username=user_in.username)


def get_user_by_id(user_id: int) -> User | None:
    return storage.users.get(user_id)

