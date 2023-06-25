from typing import TYPE_CHECKING

from sqlalchemy import (
    Column,
    Integer,
    String, Text, ForeignKey,
)
from sqlalchemy.orm import relationship, declared_attr

from .base import Base
from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Post(Base):
    @declared_attr
    def user_id(self):
        return Column(
            Integer,
            ForeignKey("user.id"),
            unique=False,
            nullable=False,  # one to many
        )

    title = Column(String(90), nullable=False)
    body = Column(Text, nullable=False, default="", server_default="")


# Обязательно импортировать в init модуля, чтобы миграха увидела эту схему!
class PostProj(db.Model, Post):
    proj_name = Column(String(50), unique=False, nullable=False)
    description = Column(String(150), unique=False, nullable=True)
    url = Column(String(150), nullable=True)
    other_contributors = Column(String(150), unique=False, nullable=True)

    # user = db.relationship(
    #     "User",
    #     backref="posts",
    #     uselist=False,  # one to one
    # )

    # @declared_attr
    # def user(self):
    #     return relationship(
    #         "User",
    #         back_populates="posts",
    #         uselist=False,  # one to one
    #     )

    def __iter__(self):
        for name_attr, value in self.__dict__.values().mapping.items():
            yield name_attr, value

    if TYPE_CHECKING:
        query: Query
