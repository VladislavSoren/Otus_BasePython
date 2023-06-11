"""
asyncio.gather

Любые синхронные действия упраздняют асинхронные, т.е. если await будет вычищен, то
код буде выполняться синхронно

aiofiles
"""

import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    filename="my_logs.log",
    filemode="w",
)
log = logging.getLogger(__name__)


async def get_users():
    log.info("get users")
    await asyncio.sleep(1)
    log.info("fetched users")
    return {"users": []}


async def get_posts():
    log.info("get posts")
    await asyncio.sleep(1)
    log.info("fetched posts")
    return {"posts": {}}


async def main():
    log.info("Start")
    # users = await get_users()
    # posts = await get_posts()
    users, posts = await asyncio.gather(
        get_users(),
        get_posts()
    )
    log.info(users)
    log.info(posts)
    log.info("Done")


if __name__ == "__main__":
    asyncio.run(main())
