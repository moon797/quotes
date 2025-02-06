from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import re
from database.userservice import *
user_router = APIRouter(tags=["Работа с сервисом"], prefix="/service")


regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def mail_checker(email: str):
    if re.fullmatch(regex, email):
        return True
    return False


class User(BaseModel):
    username: str
    email: str
    password: str


@user_router.post("/registration")
async def registration(user_model: User):
    data = dict(user_model)
    mail_validator = mail_checker(user_model.email)
    if not mail_validator:
        return {"status": 0, "message": "неправильный формат email "}
    result = registration_db(**data)
    return {"status": 1, "message": result}



@user_router.post("/login")
async def login(identificator: str, password: str):
    user = login_db(identificator=identificator, password=password)
    if user:
        return {"status": 0, "message": "Логин прошел успешно!"}
    raise HTTPException(status_code=400, detail="Неверные данные для входа. Попробуйте снова.")


