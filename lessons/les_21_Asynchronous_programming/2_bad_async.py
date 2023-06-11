"""
Ctrl + Alt + L - автоматическое форматирование кода

Внутри async функции НЕ должно быть обычного sleep! Т.к. полностью останавливается
асинхронное выполнение
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


async def get_posts():
    log.info("get posts")
    await asyncio.sleep(1)
    log.info("fetched posts")


async def main():
    log.info("Start")
    await get_users()
    await get_posts()
    log.info("Done")


if __name__ == "__main__":
    asyncio.run(main())
