DB_URL = "postgresql+psycopg2://username:passwd@0.0.0.0:9999/blog"
DB_ASYNC_URL = DB_URL.replace("psycopg2", "asyncpg")
DB_ECHO = False
# DB_ECHO = True
DB_APP_PREFIX = "blog_"

DB_POOL_SIZE = 50
DB_MAX_OVERFLOW = 10
