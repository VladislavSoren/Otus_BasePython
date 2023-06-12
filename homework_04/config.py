import os
import logging

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
    # filename="my_logs.log",
    # filemode="w",
)
log = logging.getLogger(__name__)

# os.environ[
#     "SQLALCHEMY_PG_CONN_URI"
# ] = "postgresql+asyncpg://username:secretpassword@0.0.0.0:5432/blog"
# os.environ["DB_ECHO"] = "False"
DB_ECHO = False
DB_APP_PREFIX = "home_"
