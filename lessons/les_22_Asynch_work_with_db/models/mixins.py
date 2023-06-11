from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    func,
)  # black может делать переносы в автомате


class CreatedAtMixin:
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
        nullable=False,
    )  # Запятых вконце колонок не ставь!
