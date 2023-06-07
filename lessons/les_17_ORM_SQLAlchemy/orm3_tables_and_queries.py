"""
Their syntax is identical, but LIKE is case-sensitive,
while ILIKE is case-insensitive.

"""
import uuid
from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    false, DateTime, func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    declarative_base,
    Session,
)


DB_URL = "postgresql+psycopg2://username:passwd@0.0.0.0:9999/blog"

# DB_ECHO = False
DB_ECHO = True

engine = create_engine(
    url=DB_URL,
    echo=DB_ECHO,
)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(200), unique=True, nullable=True)
    archived = Column(
        Boolean,
        default=False,
        server_default=false(),  # вызываем false, чтобы код был совместный для всех диалектов
        nullable=False,
    )
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
        nullable=False,
    )  # Запятых вконце колонок не ставь!

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, created_at={self.created_at}"

    def __repr__(self):
        return str(self)


def create_user(session: Session, username: str) -> User:
    user = User(username=username)
    print('user:', user)
    session.add(user)  # добавляем юзера в отслеживание сессии
    session.commit()
    print('Saved user', user)

    return user


def get_user_by_id(session: Session, user_id: int) -> User | None:
    user = session.get(User, user_id)
    print('user_by_id', user_id, 'value:', user)
    return user


def get_all_users(session: Session) -> list[User]:
    users = session.query(User).all()
    print('users', users)
    return users


def get_user_by_username(session: Session, username: str) -> User | None:
    user: User | None = (
        session.query(User)
        .filter_by(username=username)
        .one_or_none()  # .one() .first() .last()
    )
    print('User by username', user)
    return user


def get_users_by_username_match(session: Session, username_part: str) -> list[User]:
    users: list[User] = (
        session.query(User)
        .filter(User.id.in_([1, 2]))
        .filter(
            User.username.ilike(f"%{username_part}%"),
            User.archived.is_(False)
        )  # LIKE vs ILIKE
        .all()
    )
    print('users_by_username_match:', users)
    return users


def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    with Session(engine) as session:
        create_user(session, 'Ben')
        create_user(session, 'Tim')
        create_user(session, 'Bim')

        get_user_by_id(session, 1)
        get_user_by_id(session, 4)

        get_all_users(session)

        get_user_by_username(session, 'Tim')
        get_user_by_username(session, 'Bim')

        get_users_by_username_match(session, 'i')


if __name__ == "__main__":
    main()



