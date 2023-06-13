from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import (
    relationship,
)

from models import Base

from .mixins import CreatedAtMixin
from .posts_tags import posts_tags_assoc_table


class Tag(CreatedAtMixin, Base):
    # Columns
    name = Column(
        String(20),
        nullable=False,
        unique=True,
    )

    # Relationships
    posts = relationship(
        "Post",
        secondary=posts_tags_assoc_table,
        back_populates="tags",
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"
