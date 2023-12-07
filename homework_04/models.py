from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Text

"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

PG_CONN_URI = os.environ.get(
    "SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:example@localhost:5432/blog"

DB_ECHO = False
# DB_ECHO = True

async_engine = create_async_engine(
    url=PG_CONN_URI,
    echo=DB_ECHO,
)
Session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)


class User(Base):
    __tablename__ = 'users'

    name = Column(String(100), nullable=False, unique=False)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"name={self.name!r}, username={self.username!r}, email={self.email!r})"
        )


class Post(Base):
    __tablename__ = 'posts'

    title = Column(String(100), nullable=False)
    body = Column(Text, nullable=False)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"title={self.title!r}, user_id={self.user_id!r})"
        )

    def __repr__(self):
        return str(self)
