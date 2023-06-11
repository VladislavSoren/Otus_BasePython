"""

"""

import asyncio
import logging

import requests
from aiohttp import ClientSession

url = "https://httpbin.org/get"

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
    # filename="my_logs.log",
    # filemode="w",
)
log = logging.getLogger(__name__)


async def get_response_data(url: str):
    log.info("Start")
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            log.info("Done")
            return data


# То же самое, но в requests
def get_response_by_req_lib(url: str):
    log.info("Start")
    r_json = requests.get(url).json()
    log.info("Done")
    return r_json


async def main():
    res = await get_response_data(url)
    res2 = await get_response_data("https://jsonplaceholder.typicode.com/todos/1")
    log.info(f"res: {res}")
    log.info(f"res: {res2}")

    # res_req_json = get_response_by_req_lib(url)
    # log.info(f"res by req: {res_req_json}")


if __name__ == "__main__":
    asyncio.run(main())
