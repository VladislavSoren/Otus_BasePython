"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
import base64
from dataclasses import dataclass

from aiohttp import ClientSession

# from config import log

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
    # log.info(f"getting for {data_type} json...")
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: list[dict] = await response.json()
            # log.info(f"json for {data_type} is gotten!")
            return data


async def send_image(url: str, data):
    async with ClientSession() as session:
        async with session.post(url, json=data) as response:
            data: list[dict] = await response.json()
            return data


def image_bytes_to_str(im_path):
    with open(im_path, mode='rb') as file:
        image_bytes = file.read()
    image_str = base64.encodebytes(image_bytes).decode('utf-8')
    return image_str


async def main():
    # url = " http://127.0.0.1:9988"
    # jsons_list: list[dict] = await fetch_json(url, 'data_type')
    # print(jsons_list)

    im_paths = {
        # "/home/soren/PycharmProjects/Otus_BasePython/homework_09/images/giraOoKa4pk.jpg",
        "/home/soren/PycharmProjects/Otus_BasePython/homework_09/images/HUAX6X2xm7k.jpg",
        # "/home/soren/PycharmProjects/Otus_BasePython/homework_09/images/iS44rt72SnU.jpg",
    }

    for im_path in im_paths:
        data = {}

        data['image'] = image_bytes_to_str(im_path)
        data['user'] = 'Soren'

        url = " http://127.0.0.1:9988/image"
        jsons_list: list[dict] = await send_image(url, data)

    return jsons_list




if __name__ == "__main__":
    asyncio.run(main())