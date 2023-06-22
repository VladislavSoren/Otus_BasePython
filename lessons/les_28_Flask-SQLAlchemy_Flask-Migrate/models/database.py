__all__ = ("db",)  # Подсказка: импортируем из этого модуля только "db"

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
