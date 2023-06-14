"""
СЛОЙ ВЗАИМОДЕЙСТВИЯ С ДАННЫМИ

CRUD (Create Read Update Delete)

Модуль с функциями выполнения запрошенных действий

"""

from sqlalchemy.orm import Session

from .schemas import UserIn

from models import User


def get_users(session: Session) -> list[User]:
    return session.query(User).all()


def create_user(session: Session, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    session.add(user)
    session.commit()
    return user


def get_user_by_id(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)


def get_user_by_token(session: Session, token: str) -> User | None:
    return session.query(User).filter(User.token == token).one_or_none()
