"""
CRUD (Create Read Update Delete)
"""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserIn
from models import User


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def create_user(session: AsyncSession, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    session.add(User)
    await session.commit()
    # await session.refresh()
    return user


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def get_user_by_token(session: AsyncSession, token: str) -> User | None:
    stmt = select(User).where(User.token == token)
    result: Result = await session.execute(stmt)
    return result.scalar_one_or_none()
