import uvicorn
from fastapi import FastAPI

from items_views import router as items_router
from users.views import router as users_router
from users.view_ping_pong import router as ping_pong_router

app = FastAPI(
    # docs_url=None,
)
app.include_router(
    items_router,
    prefix='/items',
)
app.include_router(
    users_router,
    prefix='/users',
)
app.include_router(
    ping_pong_router,
    prefix='/ping',
)

# Обработка запроса на корень нашего сервиса
@app.get("/")
def index():
    return {
        "message: Index!"
    }


@app.get("/hello")
def hello(name: str = 'Soren', last_name: str='Sid'):
    return {
        f"message: Hello {name} {last_name}!"
    }


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
    )
