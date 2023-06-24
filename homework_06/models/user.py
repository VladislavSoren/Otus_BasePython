from typing import TYPE_CHECKING

from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from .base import Base
from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


# Обязательно импортировать в init модуля, чтобы миграха увидела эту схему!
class User(db.Model, Base):

    name = Column(String, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=True)
    profession_type = Column(String(50), nullable=True)
    website = Column(String(150), unique=True, nullable=True)

    # posts = relationship(
    #     "Post",
    #     back_populates="user",
    #     uselist=True,
    # )

    if TYPE_CHECKING:
        query: Query
