from datetime import datetime

from sqlalchemy import (  # black может делать переносы в автомате
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import (
    relationship,
)

from models import Base, User

from .mixins import CreatedAtMixin


class Author(CreatedAtMixin, Base):
    name = Column(String(100), nullable=False)

    user_id = Column(
        Integer,
        ForeignKey("blog_users.id"),
        nullable=False,
        unique=True,
    )

    bio = Column(
        Text,
        default="",
        server_default="",  # вызываем false, чтобы код был совместный для всех диалектов
        nullable=False,
    )

    # Эти поля никак не свзяаны с SQL БД
    # Они нужны для того чтобы мы могли в коде обращаться к СВЯЗАННЫМ сущностям
    user = relationship(
        "User",
        back_populates="author",
        uselist=False,  # 1 к 1
    )

    posts = relationship(
        "Post",
        back_populates="author",
        uselist=True,  # 1 ко многим
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, user_id={self.user_id}"

    def __repr__(self):
        return str(self)
