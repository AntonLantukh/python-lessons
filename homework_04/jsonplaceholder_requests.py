from typing import Any
from aiohttp import ClientResponse, ClientSession
import asyncio

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"


async def parse_json(response: ClientResponse):
    data: dict = await response.json()
    return data


async def get(session: ClientSession, url: str) -> Any:
    response = await session.get(url=url)
    json = await parse_json(response)
    return json


async def post(session: ClientSession, url: str, data: dict) -> dict:
    response = await session.post(url=url, data=data)
    json = await parse_json(response)
    return json


async def patch(session: ClientSession, url: str, data: dict) -> dict:
    response = await session.patch(url=url, data=data)
    json = await parse_json(response)
    return json


async def delete(session: ClientSession, url: str) -> dict:
    response = await session.delete(url=url)
    json = await parse_json(response)
    return json


async def get_users(session: ClientSession) -> list[dict]:
    data = await get(session=session, url=USERS_DATA_URL)
    return data


async def get_user(session: ClientSession, id: int) -> dict:
    url = USERS_DATA_URL + str(id)
    data = await get(session=session, url=url)
    return data


async def create_user(session: ClientSession, body: dict) -> dict:
    data = await post(session, USERS_DATA_URL, data=body)
    return data


async def update_user(session: ClientSession, body: dict, id: int) -> dict:
    url = USERS_DATA_URL + str(id)
    data = await patch(session=session, url=url, data=body)
    return data


async def delete_user(session: ClientSession, id: int) -> dict:
    url = USERS_DATA_URL + str(id)
    data = await delete(session=session, url=url)
    return data


async def get_posts(session: ClientSession) -> list[dict]:
    data = await get(session=session, url=POSTS_DATA_URL)
    return data


async def get_post(session: ClientSession, id: int) -> dict:
    url = POSTS_DATA_URL + str(id)
    data = await get(session=session, url=url)
    return data
