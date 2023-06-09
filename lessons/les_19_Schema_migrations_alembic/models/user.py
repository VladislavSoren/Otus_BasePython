from datetime import datetime

from sqlalchemy import (  # black может делать переносы в автомате
    Column,
    Integer,
    String,
    Boolean,
    false,
    DateTime,
    func,
    Text,
)
from sqlalchemy.orm import (
    relationship,
)


# from lessons.les_18_SQLAlchemy_tables_relationships.models import Base
from models import Base

from .mixins import CreatedAtMixin


class User(CreatedAtMixin, Base):

    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(200), unique=True, nullable=True)
    archived = Column(
        Boolean,
        default=False,
        server_default=false(),  # вызываем false, чтобы код был совместный для всех диалектов
        nullable=False,
    )

    # bio = Column(
    #     Text,
    #     default="",
    #     server_default="",  # вызываем false, чтобы код был совместный для всех диалектов
    #     nullable=False,
    # )

    # Эти поля никак не свзяаны с SQL БД
    # Они нужны для того чтобы мы могли в коде обращаться к СВЯЗАННЫМ сущностям
    author = relationship(
        "Author",
        back_populates="user",
        uselist=False,
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, created_at={self.created_at}"

    def __repr__(self):
        return str(self)
