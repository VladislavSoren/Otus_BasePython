
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import (
    sessionmaker,
)

import config

async_engin = create_async_engine(
    config.DB_ASYNC_URL,
    echo=config.DB_ECHO,
)
async_session = sessionmaker(
    async_engin,
    # истекает_при_фиксации=False -> можно не использовать refresh, т.к. мы работаем с нашей моделью данных (а она збс)
    expire_on_commit=False,
    class_=AsyncSession
)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
        session.rollback()
