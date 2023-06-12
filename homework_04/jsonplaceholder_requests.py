"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
from dataclasses import dataclass

from aiohttp import ClientSession

from config import log

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


@dataclass
class User:
    name: str
    username: str
    email: str


@dataclass
class Post:
    user_id: int
    title: str
    body: str


# Getting list[json]
async def fetch_json(url: str, data_type: str) -> list[dict]:
    log.info(f"getting for {data_type} json...")
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: list[dict] = await response.json()
            log.info(f"json for {data_type} is gotten!")
            return data


# Getting list[User]
async def get_users_list(url: str, data_type: str) -> list[User]:
    jsons_list: list[dict] = await fetch_json(url, data_type)
    users_list = [
        User(
            name=json_user["name"],
            username=json_user["username"],
            email=json_user["email"],
        )
        for json_user in jsons_list
    ]

    log.info(f"Parsing for {data_type} is finished!")
    return users_list


# Getting list[User]
async def get_posts_list(url: str, data_type: str) -> list[Post]:
    jsons_list: list[dict] = await fetch_json(url, data_type)
    posts_list = [
        Post(
            user_id=json_post["userId"],
            title=json_post["title"],
            body=json_post["body"],
        )
        for json_post in jsons_list
    ]

    log.info(f"Parsing for {data_type} is finished!")
    return posts_list


async def main():
    users, posts = await asyncio.gather(
        get_users_list(USERS_DATA_URL, f"{USERS_DATA_URL}".split("/")[-1]),
        get_posts_list(POSTS_DATA_URL, f"{POSTS_DATA_URL}".split("/")[-1]),
    )
    return users, posts


if __name__ == "__main__":
    asyncio.run(main())
