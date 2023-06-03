"""
Схемы (правила) передачи данных между клиентом и сервером

"""

from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str = Field(..., example="Ben",
                          min_length=3,
                          max_length=20,)


class UserIn(UserBase):
    ...


class UserOut(UserBase):
    id: int = Field(..., example=1234)  # добавляем ещё один атрибут "id"


class User(UserBase):
    id: int








