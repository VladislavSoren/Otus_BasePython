"""
Очередь позволяет НЕ ждать пока мы ВСЕХ подготовим,
а обрабатывать каждого по МЕРЕ его готовности, т.е. готов - обработали,
к следующему

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

stop = object()


async def producer(queue: asyncio.Queue, n_items: int):
    """
    generate new items
    :return:
    """
    items = []
    for i in range(1, n_items + 1):
        log.info(f"🔨 Start producing item {i}")

        # call to db / api
        # ex: fetch data
        await asyncio.sleep(0.1)
        item = {"id": i}
        log.info(f"⚒ Produced item {item}")

        await queue.put(item)

    await queue.put(stop)
    log.info("Done preparing")


async def consumer(queue: asyncio.Queue):
    """
    consume generate items
    :param items:
    :return:
    """

    while True:
        log.info(f"🍽 Start consuming")

        item = await queue.get()
        if item is stop:
            break

        # call to db / api
        # ex: create data
        await asyncio.sleep(0.2)
        log.info(f"💤 Consumed item {item}")

    log.info("✅ Done consuming")


async def main():
    log.info("Start")
    queue = asyncio.Queue()

    await asyncio.gather(
        producer(queue, 10),
        consumer(queue)
    )

    # await producer(queue, 10)
    # await consumer(queue)

    log.info("End")

    # res = await queue.get()
    # res = queue.get_nowait()  # чтобы НЕ зависнуть в случае пустой очереди (без await!)
    # log.info(f"res: {res}")


if __name__ == "__main__":
    asyncio.run(main())
