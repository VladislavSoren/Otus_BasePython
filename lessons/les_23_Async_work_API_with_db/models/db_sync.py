# from __init__ import config  # временная шняга на момент отладки
import config  # в проде

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

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)


# Зависимость нужна для того чтобы при работе с views получать актуальную сессию
# yield потому что...
def get_session() -> Session:
    with Session(engine) as session:
        yield session
        # cleanup (optional)
        session.rollback()


if __name__ == "__main__":
    # main()
    pass