"""
Когда мы импортируем Base в main.py, то вместе с ним
импортируется и юзер
Обязательно нужно делать данную инициализацию!
"""

# Путевой кастыль
from pathlib import Path
import sys

BD_PATH = Path(__file__).parent.parent
sys.path.append(str(BD_PATH))
print(*sys.path, sep="\n")

import config

from models.base import Base
from models.user import User  #!!!
from models.author import Author  #!!!
from models.post import Post
from models.tag import Tag
from models import db_sync

# from models.posts_tags import posts_tags_assoc_table


pass
