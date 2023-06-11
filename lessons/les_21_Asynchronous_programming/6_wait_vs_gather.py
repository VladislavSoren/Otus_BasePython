"""
await asyncio.wait(tasks) - задачи выполняются НЕ зависимо (ошибка НЕ останавливает других задач)
await asyncio.gather(*tasks) - задачи выполняются ЗАВИСИМО (ошибка останавливает другие задачи)
"""

import asyncio
import logging
from random import random

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
    filename="my_logs.log",
    filemode="w",
)
log = logging.getLogger(__name__)


async def get_user(user_id):
    sleep_time = round(.5 + random(), 3)
    log.info(f"get user {user_id} sleep for {sleep_time}")
    await asyncio.sleep(sleep_time)
    if random() > 0.5:
        log.warning(f"error user {user_id}")
        user_id / 0
    log.info(f"fetched user {user_id}")
    return {f"data": {'id': user_id}}


async def get_n_users(n_users):
    log.info(f"Start getting {n_users} users")
    tasks = {
        asyncio.create_task(get_user(user_id), name=f"u{user_id}")
        for user_id in range(1, n_users + 1)
    }
    done, pending = await asyncio.wait(tasks)

    # Пока это бутофория
    for task in pending:
        task.cansel()

    # Проверяем на ошибки завершённые задачи
    for task in done:
        error = task.exception()
        if error:
            log.warning(
                f"task {task.get_name()} error {error}",
                # exc_info=error,
            )
            continue
        res = task.result()
        log.info(f"task {task.get_name()} result {res}", )

    # await asyncio.gather(*tasks)
    log.info("Done")


async def main():
    log.info("Start")
    await get_n_users(5)


if __name__ == "__main__":
    asyncio.run(main())
