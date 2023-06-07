from datetime import datetime

from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Text,
    DateTime,
    func,
)

DB_URL = "sqlite:///example1.db"

# DB_ECHO = False # обычно должен быть False
DB_ECHO = True

engine = create_engine(
    url=DB_URL,
    echo=DB_ECHO,  # Флаг, который говорит, что любой SQL запрос можно вывести в консоль (збс ТОЛЬКО для дебага)
)

# Содержит данные о таблицах (от туда можно будет брать нужную инфу, не трогая таблицы)
metadata = MetaData()

authors_table = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(20), unique=True, nullable=False),
    Column("email", String(150), unique=True, nullable=True),
    Column(
        "bio",
        Text,
        nullable=False,
        default="hello",
        server_default=""),  # server_default - со стороны БД
    Column(
        "created_at",
        DateTime,
        default=datetime.utcnow,
        server_default=func.now()),
)


def main():
    # print(metadata.tables)
    metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()












































