"""
Когда мы импортируем Base в main.py, то вместе с ним
импортируется и юзер
Обязательно нужно делать данную инициализацию!
"""

from .base import Base
from .user import User  #!!!
from .author import Author  #!!!
from .post import Post
