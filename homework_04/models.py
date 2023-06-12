"""
- создайте алхимичный engine
- добавьте declarative base (свяжите с engine)
- создайте объект Session
- добавьте модели User и Post, объявите поля:
- для модели User обязательными являются name, username, email
- для модели Post обязательными являются user_id, title, body
- создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr, relationship

import config

PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost/postgres"
)

# creation of async engin
async_engin = create_async_engine(
    PG_CONN_URI,
    echo=config.DB_ECHO,
)


# Declare base class
class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{config.DB_APP_PREFIX}{cls.__name__.lower()}s"

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True)


# creation of declarative_base and AsyncSession
Base = declarative_base(cls=Base)
Session = sessionmaker(
    async_engin,
    # истекает_при_фиксации=False -> можно не использовать refresh, т.к. мы работаем с нашей моделью данных (а она збс)
    expire_on_commit=False,
    class_=AsyncSession,
)


# Declare other classes
class User(Base):
    name = Column(String(30), unique=False, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=True)

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )


class Post(Base):
    user_id = Column(
        Integer,
        ForeignKey("home_users.id"),
        unique=False,
        nullable=False,  # one to many
    )
    title = Column(String(90), nullable=False)
    body = Column(Text, nullable=False, default="", server_default="")

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,  # one to one
    )
