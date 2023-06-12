"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.models import Base, async_engin, User, Post
from jsonplaceholder_requests import main as get_users_and_posts
from jsonplaceholder_requests import User as User_DC
from jsonplaceholder_requests import Post as Post_DC

from config import log
from models import Session


# database schema re-creation function
async def init_tables():
    async with async_engin.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with async_engin.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# I/O functions
async def create_user(session: AsyncSession, user: User_DC) -> User:
    user = User(
        name=user.name,
        username=user.username,
        email=user.email,
    )
    session.add(user)

    try:
        await session.commit()
    except Exception as e:
        pass

    return user


async def create_users(local_session: Session, users: list[User_DC]):
    async with local_session() as session:
        for user in users:
            await create_user(session, user)
        log.info("users saved in DB")


async def create_post(session: AsyncSession, post: Post_DC) -> Post:
    post = Post(
        user_id=post.user_id,
        title=post.title,
        body=post.body,
    )
    session.add(post)
    await session.commit()

    return post


async def create_posts(local_session: Session, posts: list[Post_DC]):
    async with local_session() as session:
        for post in posts:
            await create_post(session, post)
        log.info("posts saved in DB")


async def async_main():
    # database schema re-creation
    async with Session() as session:
        await init_tables()

    # getting users and posts from web
    users_objs, posts_objs = await get_users_and_posts()

    await asyncio.gather(
        create_users(Session, users_objs),
        create_posts(Session, posts_objs),
    )


# async def async_main():
#     async with Session() as session:
#         # database schema re-creation
#         await init_tables()
#
#         # getting users and posts from web
#         users_objs, posts_objs = await get_users_and_posts()
#
#         await asyncio.gather(
#             create_users(session, users_objs),
#             create_posts(session, posts_objs),
#         )
#
#         # await create_users(session, users_objs)
#         # await create_posts(session, posts_objs)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
