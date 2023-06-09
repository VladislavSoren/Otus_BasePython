from sqlalchemy import (
    create_engine,
    # update,
    func,
)

from sqlalchemy.orm import (
    declarative_base,
    Session,
    joinedload, selectinload,
)

from lessons.les_18_SQLAlchemy_tables_relationships.config import DB_URL, DB_ECHO
from lessons.les_18_SQLAlchemy_tables_relationships.models import (
    Base,
    User,
    Author,
    Post,
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


def main():
    with Session(engine) as session:
        ben = create_user(session, 'Ben')
        tim = create_user(session, 'Tim')

        author_ben = create_author(session, "Big Ben", user=ben)
        author_tim = create_author(session, "Team-building", user=tim)

        Sam = create_user(session, 'Sam')
        Pit = create_user(session, 'Pit')

        show_users_with_authors(session)

        show_authors_with_users(session)

        show_users_only_with_authors(session)

        update_users_emails_by_username(session, "@google.com")
        update_users_emails_by_username(session,
                                        "@foo.com",
                                        func.length(User.username) == 4,
                                        ),

        find_authors_by_user_email_domain(session, "@foo.com")

        author_ben = find_authors_by_user_username(session, "Tim")
        create_post(session, author_ben, 'Cat', 'Hat')

        show_users_with_author_and_posts(session)

        show_authors_with_users_and_posts(session)

        pass


if __name__ == '__main__':
    main()


