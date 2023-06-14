"""

"""

import asyncio

import logging

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
    # filename="my_logs.log",
    # filemode="w",
)
log = logging.getLogger(__name__)


async def producer(n_items: int):
    """
    generate new items
    :return:
    """
    items = []
    for i in range(1, n_items + 1):
        # call to db / api
        # ex: fetch data
        await asyncio.sleep(0.1)
        item = {"id": i}
        log.info(f"Prepared item {item}")
        items.append(item)

    log.info("Done preparing")
    return items


async def consumer(items: list[dict]):
    """
    consume generate items
    :param items:
    :return:
    """
    for item in items:
        # call to db / api
        # ex: create data
        await asyncio.sleep(0.1)
        log.info(f"Consumed item {item}")

    log.info("Done consuming")


async def main():
    items = await producer(10)
    await consumer(items)


if __name__ == "__main__":
    asyncio.run(main())
