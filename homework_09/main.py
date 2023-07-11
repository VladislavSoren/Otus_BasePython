import asyncio
import base64
import io
import os
from dataclasses import dataclass

import numpy as np
from PIL import Image
from aiohttp import ClientSession


# from config import log


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


async def get_prediction(url: str, data):
    async with ClientSession() as session:
        async with session.post(url, json=data) as response:
            data: dict = await response.json()
            return data


def image_bytes_to_str(im_path):
    with open(im_path, mode='rb') as file:
        image_bytes = file.read()
    image_str = base64.encodebytes(image_bytes).decode('utf-8')
    return image_str


def show_input_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    image.show()


SEX_AGE_HUMANS_DETECTION_SERVICE_URL = " http://127.0.0.1:9988/image"


async def main():
    im_path = "/home/soren/PycharmProjects/Otus_BasePython/homework_09/images/HUAX6X2xm7k.jpg"

    # serialization
    data = {}
    data['user'] = 'Soren'
    data['image'] = image_bytes_to_str(im_path)
    data['image_name'] = os.path.basename(im_path)

    # sending image to service and receiving  response with tagged image
    json_input: dict = await get_prediction(SEX_AGE_HUMANS_DETECTION_SERVICE_URL, data)

    #  deserialization
    image_bytes = base64.b64decode(json_input["tagged_img"])

    # displaying tagged image
    show_input_image(image_bytes)


if __name__ == "__main__":
    asyncio.run(main())
