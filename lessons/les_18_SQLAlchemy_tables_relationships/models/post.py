from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import (
    relationship,
)

from lessons.les_18_SQLAlchemy_tables_relationships.models import Base


class Post(Base):

    # Columns
    title = Column(
        String(90),
        nullable=False,
    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )
    author_id = Column(
        Integer,
        ForeignKey("blog_authors.id"),
        unique=False,
        nullable=False,
    )

    # Relationships
    author = relationship(
        "Author",
        back_populates="posts",
        uselist=False,
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, author_id={self.author_id})"