from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg://username:password@pg:5432/diary",
)


class Config:
    DEBUG = False
    SECRET_KEY = ""
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = "..."  # read from secret file


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = "test_key"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
