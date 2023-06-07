from fastapi import APIRouter, HTTPException, status, Depends

from .schemas import UserOut, UserIn, User
from . import crud
from . dependencies import get_user_by_auth_token

router = APIRouter(
    tags=['my_views'],
)


# Новый viewer
@router.get(
    "/",
    response_model=dict[str, str],
    # Переопределяем статусы ошибок
)
def ping_pong() -> dict[str, str]:
    pong_answer: dict[str, str] = crud.get_pong()
    # Условие "if pong_answer" заменено, т.к. пустой словарь - тоже нормальный ответ
    if pong_answer is not None:
        return pong_answer
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User №{pong_answer} is not found!"
    )
