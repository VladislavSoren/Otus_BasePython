__all__ = ("Base",)  # перечень объектов на экспорт из модуля

# Путевой кастыль
from pathlib import Path
import sys

# BD_PATH = Path(__file__).parent / 'db'
BD_PATH = Path(__file__).parent.parent
# print('Путь к директории с БД:', BD_PATH)
sys.path.append(str(BD_PATH))
# print(*sys.path, sep='\n')

from sqlalchemy import (  # black может делать переносы в автомате
    Column,
    Integer,
    String,
    Boolean,
    false,
    DateTime,
    func)

from sqlalchemy.orm import declarative_base, declared_attr

import config



class Base:

    @declared_attr
    def __tablename__(cls):
        return f"{config.DB_APP_PREFIX}{cls.__name__.lower()}s"

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)
# print(Base.mro())

