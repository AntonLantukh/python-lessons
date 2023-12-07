import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from aiohttp import ClientSession

from jsonplaceholder_requests import get_users, get_posts
from models import Base, Post, User, Session, async_engine

"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""


def create_post(
    user_id: int,
    title: str,
    body: str
) -> Post:
    post = Post(
        title=title,
        body=body,
        user_id=user_id,
    )

    return post


def create_user(
    name: int,
    username: str,
    email: str
) -> User:
    user = User(
        name=name,
        username=username,
        email=email,
    )

    return user


async def create_users(session: AsyncSession, data: list[dict]):
    users = [create_user(
        name=user["name"],
        username=user["username"],
        email=user["email"],
    ) for user in data]

    session.add_all(users)
    await session.commit()


async def create_posts(session: AsyncSession, data: list[dict]):
    posts = [create_post(
        user_id=post["userId"],
        title=post["title"],
        body=post["body"],
    ) for post in data]

    session.add_all(posts)
    await session.commit()


async def async_main():
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

    async with ClientSession() as session:
        users_data, posts_data = await asyncio.gather(
            get_users(session),
            get_posts(session),
        )

    async with Session() as session:
        await create_users(session, users_data)
        await create_posts(session, posts_data)


if __name__ == "__main__":
    asyncio.run(async_main())
