from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    ""
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
