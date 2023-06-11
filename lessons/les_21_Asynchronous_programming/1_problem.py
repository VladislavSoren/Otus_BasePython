"""
В реальном продуктовом коде НЕ должно быть никаких sleep
"""

import logging
from time import sleep

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    filename='my_logs.log',
    filemode='w',
)
log = logging.getLogger(__name__)

def get_users():
    log.info("get users")
    sleep(1)
    log.info("fetched users")

def get_posts():
    log.info("get posts")
    sleep(1)
    log.info("fetched posts")


def main():
    log.info("Start")
    get_users()
    get_posts()
    log.info("Done")


if __name__ == "__main__":
    main()
