from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DB_FILE = BASE_DIR / "app.db"

DEFAULT_DB_URL = "postgresql+psycopg2://username:passwd@172.18.0.2:5432/blog"

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    DEFAULT_DB_URL,
)


class Config(object):
    TESTING = False
    DEBUG = False
    SECRET_KEY = "7ec26d07b86e8204645c637dacf21be3"
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    SECRET_KEY = "f260e09979ef96ce87ed16afdd2dc77b"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
