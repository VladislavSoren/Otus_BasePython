from typing import Iterable
from datetime import datetime

from sqlalchemy import (
    create_engine,
    # update,
    func, or_,
)

from sqlalchemy.orm import (
    declarative_base,
    Session,
    joinedload, selectinload, aliased,
)

from lessons.les_20_Complex_db_relationships.config import DB_URL, DB_ECHO
from lessons.les_20_Complex_db_relationships.models import (
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


def create_user(session: Session, username: str) -> User:
    user = User(username=username)
    print('user:', user)
    session.add(user)  # добавляем юзера в отслеживание сессии
    session.commit()
    print('Saved user', user)

    return user


# def create_author(session: Session, name: str, user_id: int) -> Author:
def create_author(session: Session, name: str, user: User) -> Author:
    author = Author(
        name=name,
        # user_id=user
        user=user
    )
    session.add(author)
    session.commit()
    print("created author", author)

    return author


def create_post(session: Session, author: Author, *titles: str) -> list[Post]:

    posts = [
        Post(
            title=title,
            author_id=author.id
        )
        for title in titles
    ]
    session.add_all(posts)
    session.commit()
    print('posts:', posts)
    return posts


def create_tags(session: Session, *names: str) -> list[Tag]:

    tags = [
        Tag(
            name=name,
        )
        for name in names
    ]
    session.add_all(tags)
    session.commit()
    print('tags:', tags)
    return tags


def find_tags(session: Session, *names: str) -> list[Tag]:
    tags = session.query(Tag).filter(
        func.lower(Tag.name).in_(names)
    ).all()
    print("found tags:", tags)

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


def show_users_with_authors(session: Session):
    # N+1 problem
    users = (
        session
        .query(User)
        .options(joinedload(User.author))
        .all()
    )
    for user in users:
        print('User', user, 'is', user.author)


def show_authors_with_users(session: Session):
    authors = (
        session
        .query(Author)
        .options(joinedload(Author.user))
        .all()
    )
    for author in authors:
        print('Author', author, 'is', author.user)


def show_users_only_with_authors(session: Session):
    # N+1 problem
    users = (
        session
        .query(User)
        # .join(User.author)  # isouter=False
        .options(joinedload(User.author, innerjoin=True))
        # .filter(User.id.isnot(None))
        .all()
    )

    # Получив юзеров методом .join, при ка каждом обращении к ним будет использоваться вспомогательный SQL запрос
    # При joinedload вспомогательных запросов НЕ будет, а сразу будет происходить обращение к объектам!
    for user in users:
        print('User', user, 'is', user.author)


def update_users_emails_by_username(session: Session, domain: str, *filters):
    # (
    #     session
    #     .query(User)
    #     .filter(*filters)
    #     .update({
    #         User.email: User.username + domain
    #     })
    # )
    query = session.query(User).filter(*filters)
    query.update(
        {
            User.email: User.username + domain,
        },
        synchronize_session=False,  # обновление сущностей
    )
    session.commit()


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


def find_authors_by_user_username(session: Session, username: str):

    author = (
        session
        .query(Author)
        # .options(joinedload(Author.user, innerjoin=True))
        .join(Author.user)  # а joinedload НЕ сработал!
        .filter(User.username == username)
        .one()
    )

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


def find_posts_by_title(session: Session, *texts: str) -> Iterable[Post]:
    posts = (
        session.query(Post)
        .filter(
            or_(
                *(
                    func.lower(Post.title).contains(text.lower())
                    for text in texts
                )
            )
        )
        .order_by(Post.id)
        .all()
    )

    print(posts)

    return posts


def add_tags_to_posts(session: Session, posts: Iterable[Post], tags: Iterable[Tag]):
    for post in posts:
        for tag in tags:
            if tag not in post.tags:
                post.tags.append(tag)

    session.commit()


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


def main():
    with Session(engine) as session:
        # ben = create_user(session, 'Ben')
        # tim = create_user(session, 'Tim')
        #
        # author_ben = create_author(session, "Big Ben", user=ben)
        # author_tim = create_author(session, "Team-building", user=tim)
        #
        # Sam = create_user(session, 'Sam')
        # Pit = create_user(session, 'Pit')
        #
        # show_users_with_authors(session)
        #
        # show_authors_with_users(session)
        #
        # show_users_only_with_authors(session)
        #
        # update_users_emails_by_username(session, "@google.com")
        # update_users_emails_by_username(session,
        #                                 "@foo.com",
        #                                 func.length(User.username) == 4,
        #                                 ),
        #
        # find_authors_by_user_email_domain(session, "@foo.com")
        #
        # author_ben = find_authors_by_user_username(session, "Tim")
        # create_post(session, author_ben, 'Cat', 'Hat')
        #
        # show_users_with_author_and_posts(session)
        #
        # show_authors_with_users_and_posts(session)

        # create_tags(session, 'cat python', 'hat docker')

        # author_tim = find_authors_by_user_username(session, "Tim")
        # tags = find_tags(session, 'news', 'python', 'git')
        # create_post_with_tags(session,author_tim, "New Python Tool", tags)

        # auto_assoc_tags_with_posts(session)

        # find_posts_with_any_of_tags(session, 'python', 'git')

        # find_posts_for_two_tags(session, 'python', 'docker')

        find_posts_for_all_of_tags(session, 'python', 'git')

        pass


if __name__ == '__main__':
    main()


