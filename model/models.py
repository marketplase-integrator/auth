import re
from typing import Any, Self

from pydantic import BaseModel, EmailStr, Field, validator



class User(BaseModel):
    name: str = Field(min_lengt=3, max_length=15)
    email: EmailStr
    password: str

    @validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("в пароле должно быть минимум 8 символов")
        if not any(c.isupper() for c in value):
            raise ValueError("в пароле должна быть заглавная буква")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Пароль должен иметь хотя бы один спец.символ")
        if not(c.isdigit() for c in value):
            raise ValueError("Пароль должен иметь хотя бы одну цифру")
        return value

try:
    user = User(name = "Михаил",
                email = "Mikhail2121@gmail.com",
                password = "1Qwerty}")
    print(user.model_dump())
except ValueError as e:
        print(f"Ошибка:{e}")