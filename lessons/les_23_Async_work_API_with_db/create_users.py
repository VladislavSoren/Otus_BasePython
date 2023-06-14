from time import time
from sqlalchemy.orm import (
    Session,
)

from models import User
from models.db_sync import engine


def create_users(session: Session, n_users: int):
    t = time() % 100  # подставятся последние 2 цифры от времени (хитро)
    users = [
        User(username=f"user_{i:03d}_{t}")
        for i in range(1, n_users + 1)
    ]
    session.add_all(users)
    session.commit()


# Зависимость нужна для того чтобы при работе с views получать актуальную сессию
# yield потому что...
def main():
    count = 1000
    with Session(engine) as session:
        create_users(session, count)


if __name__ == "__main__":
    main()
