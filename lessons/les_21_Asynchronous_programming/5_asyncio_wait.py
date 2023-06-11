"""
asyncio.create_task
asyncio.wait(tasks)
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


async def get_user(user_id):
    log.info("get users")
    await asyncio.sleep(1)
    log.info("fetched users")
    return {f"data": {'id': user_id}}


async def get_n_users(n_users):
    log.info(f"Start getting {n_users} users")
    tasks = {
        asyncio.create_task(get_user(user_id))
        for user_id in range(1, n_users + 1)
    }
    await asyncio.wait(tasks)
    log.info("Done")


async def main():
    log.info("Start")
    await get_n_users(5)


if __name__ == "__main__":
    asyncio.run(main())