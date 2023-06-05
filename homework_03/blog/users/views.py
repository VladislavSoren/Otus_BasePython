"""
СЛОЙ ВЗАИМОДЕЙСТВИЯ С СЕТЬЮ

Здесь view функции (едставления)

По сути готовим контракт с фронтендом:
Без внутренней логики прописываем, что принимаем и отдаём
"""

from fastapi import APIRouter, HTTPException, status, Depends

from .schemas import UserOut, UserIn, User
from . import crud
from . dependencies import get_user_by_auth_token

router = APIRouter(
    tags=['Users'],
)


@router.get(
    "/",
    response_model=list[UserOut],
)
def get_users():
    # raise NotImplemented
    return crud.get_users()


# Функция get_me зависит от функции передачи юзера по токену get_user_by_auth_token
@router.get('/me', response_model=UserOut)
def get_me(user: User = Depends(get_user_by_auth_token)):
    return user


@router.post(
    "/",
    response_model=UserOut,
    description='Creates a user',
)
def create_user(user_in: UserIn):
    return crud.create_user(user_in=user_in)


@router.get(
    "/{user_id}",
    response_model=UserOut,
    # Переопределяем статусы ошибок
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "detail": {
                                "title": "Detail",
                                "type": "string",
                                "example": "User!!! #0 not found!",
                            },
                        },
                    }
                }
            },
        },
    },
)
def get_user_by_id(user_id: int) -> User:
    user: User | None = crud.get_user_by_id(user_id=user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User №{user_id} is not found!"
    )


# Новый viewer
@router.get(
    "/ping/",
    response_model=dict[str, str],
    # Переопределяем статусы ошибок
)
def ping_pong() -> dict[str, str]:
    pong_answer: dict[str, str] = crud.get_pong()
    if pong_answer:
        return pong_answer
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User №{pong_answer} is not found!"
    )








