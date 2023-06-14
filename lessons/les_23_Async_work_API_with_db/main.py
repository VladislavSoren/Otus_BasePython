import uvicorn
from fastapi import FastAPI

from items_views import router as items_router

# from lessons.les_23_Async_work_API_with_db.views.users.views import router as users_router
from views.users_sync import router as users_sync_router
from views.users_async import router as users_async_router

app = FastAPI(
    # docs_url=None,
)
app.include_router(
    items_router,
    prefix="/items",
)
app.include_router(
    users_async_router,
    prefix="/users/async",
)
app.include_router(
    users_sync_router,
    prefix="/users/sync",
)


# Обработка запроса на корень нашего сервиса
@app.get("/")
def index():
    return {"message: Index!"}


@app.get("/hello")
def hello(name: str = "Soren", last_name: str = "Sid"):
    return {f"message: Hello {name} {last_name}!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
    )
