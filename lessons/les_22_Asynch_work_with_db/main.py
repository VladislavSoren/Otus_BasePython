"""
Любое I/O действие при асинхронке требует повышенного внимания, от сюда
expire_on_commit, refresh и т.п.

scalars() - возвращает генератор, т.е. один раз сможем только проитерироваться
scalars().all() - возвращает список, уитерируйся (но RAM)
.distinct() - даёт возможность подтягивать только уникальные строчки (SELECT DISTINCT)
"""

import asyncio

from typing import Iterable
from datetime import datetime

from sqlalchemy import (
    create_engine,
    select,
    update,
    # update,
    func, or_,
)
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import (
    Session,
    joinedload, selectinload, aliased, sessionmaker,
)

from lessons.les_22_Asynch_work_with_db.config import DB_URL, DB_ECHO, DB_ASYNC_URL
from lessons.les_22_Asynch_work_with_db.models import (
    # Base,
    User,
    Author,
    Post,
    Tag,
)

engine = create_engine(
    url=DB_URL,
    echo=DB_ECHO,
)

async_engin = create_async_engine(
    DB_ASYNC_URL,
    echo=DB_ECHO,
)
async_session = sessionmaker(
    async_engin,
    # истекает_при_фиксации=False -> можно не использовать refresh, т.к. мы работаем с нашей моделью данных (а она збс)
    expire_on_commit=False,
    class_=AsyncSession
)


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    print('user:', user)
    session.add(user)  # добавляем юзера в отслеживание сессии
    await session.commit()  # I/O действие -> await
    # await session.refresh(user)  # если expire_on_commit=True, т.е. объект сгорел, то его нужно обновить в бд
    print('Saved user', user)

    return user


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def get_user_by_username(session: AsyncSession, username: str) -> User:
    # preparing statement
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    user: User = result.scalar_one()  # если использовать one, то вернётся кортеж с одним элементом
    print(f"user by username {username} is {user}")

    return user


# def create_author(session: Session, name: str, user_id: int) -> Author:
async def create_author(session: AsyncSession, name: str, user: User) -> Author:
    author = Author(
        name=name,
        # user_id=user
        user=user
    )
    session.add(author)
    await session.commit()
    print("created author", author)

    return author


async def create_post(session: AsyncSession, author: Author, *titles: str) -> list[Post]:
    posts = [
        Post(
            title=title,
            author_id=author.id
        )
        for title in titles
    ]
    session.add_all(posts)
    await session.commit()
    print('posts:', posts)
    return posts


async def create_tags(session: AsyncSession, *names: str) -> list[Tag]:
    tags = [
        Tag(
            name=name,
        )
        for name in names
    ]
    session.add_all(tags)
    await session.commit()
    print('tags:', tags)
    return tags


async def find_tags(session: AsyncSession, *names: str) -> list[Tag]:
    tags_stmt = (
        # tags
        select(Tag)
        # within these names
        .filter(func.lower(Tag.name).in_(names))
    )
    result: Result = await session.execute(tags_stmt)
    tags: list[Tag] = result.scalars().all()
    print("found tags", tags)

    return tags


def create_post_with_tags(
        session: Session,
        author: Author,
        title: str,
        tags: Iterable[Tag],
) -> Post:
    post = Post(
        title=title,
        author_id=author.id,
        tags=tags,
    )
    session.add(post)
    session.commit()
    print("Added post", post, 'with tags:', tags)

    return post


async def show_users_with_authors(session: AsyncSession):
    # N+1 problem (solved)
    users_stmt = (
        select(User)
        # .join(User.author)  # Убрано т.к. None тож выводим
        .options(
            joinedload(User.author)
        )
    )
    result: Result = await session.execute(users_stmt)
    users = result.scalars().all()
    # [U1, U2, U3] - with scalars call
    # [(U1, ), (U2, ), (U3, )] - w/o scalars call

    for user in users:
        print('User', user, 'is', user.author)


async def show_authors_with_users(session: AsyncSession):
    authors_stmt = (
        select(Author)
        .options(joinedload(Author.user))
    )
    result: Result = await session.execute(authors_stmt)
    authors = result.scalars().all()

    for author in authors:
        print('Author', author, 'is', author.user)


async def show_users_only_with_authors(session: AsyncSession):
    # N+1 problem
    users_stmt = (
        select(User)
        # .join(User.author)  # isouter=False
        .options(joinedload(User.author, innerjoin=True))
    )
    result: Result = await session.execute(users_stmt)
    users = result.scalars().all()

    # Получив юзеров методом .join, при ка каждом обращении к ним будет использоваться вспомогательный SQL запрос
    # При joinedload вспомогательных запросов НЕ будет, а сразу будет происходить обращение к объектам!
    for user in users:
        print('User', user, 'is', user.author)


async def update_users_emails_by_username(session: AsyncSession, domain: str, *filters):
    async with session.begin():
        stmt = (
            update(User)  # synchronize_session=False
            .where(*filters)
            .values(
                {
                    User.email: User.username + domain,
                },
            )
            .execution_options(synchronize_session=False)
        )
        await session.execute(stmt)

    # commit happens on __aexit__ for this session in context manager
    # await session.commit()


def find_authors_by_user_email_domain(session: Session, email_domain):
    authors = (
        session
        .query(Author)
        # .join(Author.user)
        .options(joinedload(Author.user, innerjoin=True))
        .filter(User.email.endswith(email_domain))
        .all()
    )

    for author in authors:
        print(author)
    return authors


async def find_author_by_user_username(session: AsyncSession, username: str):
    stmt = (
        select(Author)
        # .options(joinedload(Author.user, innerjoin=True))
        .join(Author.user)  # а joinedload НЕ сработал!
        .filter(User.username == username)
    )

    result: Result = await session.execute(stmt)
    author: Author = result.scalar_one()

    print(f'author for {username} is {author.name}')
    return author


def show_users_with_author_and_posts(session: Session):
    users = (
        # get users
        session.query(User)
        # join all related objects
        # .options(joinedload(User.author).joinedload(Author.posts))
        # joinedload - "to one"
        # selectinload - "to many"
        .options(joinedload(User.author).selectinload(Author.posts))
        # sort
        .order_by(User.id)
        # get all of them
        .all()
    )

    for user in users:
        print("- user", user)
        if not user.author:
            continue
        print("++ author", user.author)
        print("=== posts:")
        for post in user.author.posts:
            print("=", post)


def show_authors_with_users_and_posts(session: Session):
    authors = (
        # all authors
        session.query(Author)
        # join related objects
        .options(
            # "to one"
            joinedload(Author.user),
            # "to many"
            selectinload(Author.posts),
        )
        # sort
        .order_by(Author.id)
        # fetch all
        .all()
    )

    for author in authors:
        print("+", author)
        print("++", author.user)

        print("=== posts:")
        for post in author.posts:
            print("=", post)


def auto_assoc_tags_with_posts(session: Session):
    tags: Iterable[Tag] = session.query(Tag).all()
    posts: Iterable[Post] = session.query(Post).options(
        # Нагибаем проблему N + 1
        selectinload(Post.tags)  # selectinload так как связь ко многим (уберутся дубли)
    ).all()
    for post in posts:
        title = post.title.lower()
        for tag in tags:
            if (tag.name.lower() in title) and (tag not in post.tags):
                post.tags.append(tag)

    # add НЕ нужно как так у каждого поста и тега есть привязка к сесссии, т.к. мы их достали из базы
    # Завершаем транзакцию
    session.commit()


def find_posts_with_any_of_tags(session: Session, *tags_names: str) -> Iterable[Post]:
    posts: Iterable[Post] = (
        session.query(Post)
        .join(Post.tags)
        .filter(
            func.lower(Tag.name).in_(tags_names),
        )
        .options(  # если делать без опций, то лиху больше запросов
            joinedload(Post.author),
            selectinload(Post.tags)
        )
        .order_by(Post.title)
    )

    for post in posts:
        print('--------')
        print("post", post)
        print("author", post.author)
        print("tags", post.tags)

    return posts


def find_posts_for_two_tags(session: Session, tag1: str, tag2: str) -> Iterable[Post]:
    table_tags1 = aliased(Tag, name="table_tags1")
    table_tags2 = aliased(Tag, name="table_tags2")
    # table_tags3 = aliased(Tag, name="table_tags2")
    posts = (
        session.query(Post)
        .join(table_tags1, Post.tags)
        .join(table_tags2, Post.tags)
        # .join(table_tags3, Post.tags)
        .filter(
            func.lower(table_tags1.name) == tag1,
            func.lower(table_tags2.name) == tag2,
            # func.lower(table_tags3.name) == tag3,
        )
        .options(selectinload(Post.tags))
        .order_by(Post.id)
        .all()
    )

    print("posts for both tags", tag1, tag2)

    for post in posts:
        print("---")
        print("post", post)
        print("tags:", post.tags)

    return posts


def find_posts_between_dates(session: Session, after_dt: datetime, before_dt: datetime) -> Iterable[Post]:
    posts = session.query(Post).filter(
        Post.created_at >= after_dt,
        Post.created_at <= before_dt,
    ).order_by(Post.created_at).all()

    for post in posts:
        print(post.title, post.created_at)

    return posts


async def find_posts_by_title(session: AsyncSession, *texts: str) -> Iterable[Post]:
    posts_stmt = (
        select(Post)
        .filter(or_(*(func.lower(Post.title).contains(text.lower()) for text in texts)))
        .order_by(Post.id)
    )

    result: Result = await session.execute(posts_stmt)
    posts = result.scalars().all()

    for post in posts:
        print("p", post)

    return posts

async def find_posts_with_tags_by_title(
    session: AsyncSession, *texts: str
) -> Iterable[Post]:
    posts_stmt = (
        select(Post)
        .filter(or_(*(func.lower(Post.title).contains(text.lower()) for text in texts)))
        .options(selectinload(Post.tags))
        .order_by(Post.id)
    )

    result: Result = await session.execute(posts_stmt)
    posts_with_tags = result.scalars().all()

    for post in posts_with_tags:
        print("p", post)

    return posts_with_tags

async def add_tags_to_posts(
    session: AsyncSession,
    posts: Iterable[Post],
    tags: Iterable[Tag],
):
    for post in posts:
        for tag in tags:
            if tag not in post.tags:
                post.tags.append(tag)

    await session.commit()


# Мощный запрос по одновременному вхождению перечня тегов в пост
# Вернёт посты содержащие строго этот перечень
# Оптимизированынй вариант "find_posts_for_two_tags"
def find_posts_for_all_of_tags(session: Session, *tags: str) -> Iterable[Post]:
    posts_q = session.query(Post)

    tags_names = list(set(map(str.lower, tags)))
    filters = []

    for tag_name in tags_names:
        table = aliased(Tag, name=f"table_tags_{tag_name}")
        posts_q = posts_q.join(table, Post.tags)
        filters.append(
            func.lower(table.name) == tag_name,
        )

    posts = (
        posts_q
        .filter(*filters)
        .options(selectinload(Post.tags))
        .order_by(Post.id)
        .all()
    )

    print("posts for tags", tags)

    for post in posts:
        print("---")
        print("post", post)
        print("tags:", post.tags)

    return posts


async def main():
    # async with async_session() as session:
    # async with session.begin():
    async with async_session() as session:
        # ben: User = await create_user(session, 'Fil')
        # tim: User = await create_user(session, 'Tim')
        # Sam = create_user(session, 'Sam')
        # Pit = create_user(session, 'Pit')
        #
        # user_3 = await get_user_by_id(session, 3)
        # user_sam = await get_user_by_username(session, 'Sam')
        #
        # author_ben = create_author(session, "Big Ben", user=ben)
        # author_tim = create_author(session, "Team-building", user=tim)
        # author_sam: Author = await create_author(session, "Serious Sam", user=user_sam)

        # await show_users_with_authors(session)
        # await show_authors_with_users(session)
        # await show_users_only_with_authors(session)

        # update_users_emails_by_username(session, "@google.com")
        # await update_users_emails_by_username(session,
        #                                       "@great.com",
        #                                       User.username == "Sam",
        #                                       ),
        # find_authors_by_user_email_domain(session, "@foo.com")

        # author_sam = await find_author_by_user_username(session, "Sam")
        # await create_post(session, author_sam, 'Super Python', 'Mega Git')

        # show_users_with_author_and_posts(session)
        # show_authors_with_users_and_posts(session)

        # await create_tags(session, 'numpy', 'pandas')

        # posts: Iterable[Post] = await find_posts_by_title(session, "python")
        # posts: Iterable[Post] = await find_posts_with_tags_by_title(session, "python")
        # tags = await find_tags(session, "numpy")
        # await add_tags_to_posts(session, posts, tags)

        # author_tim = find_authors_by_user_username(session, "Tim")
        # tags = find_tags(session, 'news', 'python', 'git')
        # create_post_with_tags(session, author_tim, "New Python Tool", tags)

        # auto_assoc_tags_with_posts(session)

        # find_posts_with_any_of_tags(session, 'python', 'git')

        # find_posts_for_two_tags(session, 'python', 'docker')

        # find_posts_for_all_of_tags(session, 'python', 'git')

        pass


if __name__ == '__main__':
    asyncio.run(main())
