"""
Два primary_key станут одним общим

"""

from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
)

from models import Base

posts_tags_assoc_table = Table(
    "blog_posts_tags_assoc",
    Base.metadata,
    Column("post_id", ForeignKey("blog_posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("blog_tags.id"), primary_key=True),
)
