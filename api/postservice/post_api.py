from fastapi import APIRouter, HTTPException
from database.postservice import *

post_router = APIRouter(tags=["Управление пользователями"], prefix="/user")


@post_router.post("/post")
async def add_post(user_id:int, main_text:str):
    result = add_post_db(user_id=user_id, main_text=main_text)
    if result:
        return {"status": 0, "message": result}
    return {"status": 1, "message": "ошибка в добавления поста"}


@post_router.post("/comment")
async def add_comment(comment_id:int, user_id:int, main_text:str):
    result = add_comment_db(user_id=user_id, comment_id=comment_id, main_text=main_text)
    if result:
        return {"status": 0, "message": result}
    return {"status": 1, "message": "ошибка в добавления комментария"}

@post_router.delete("/post_delete/{post_id}")
async def remove_post(post_id: int):
    result = delete_post_db(post_id)
    if result:
        return {"status": 0, "message": "Пост успешно удален"}
    return {"status": 1, "message": "ошибка в удалении поста"}


@post_router.delete("/comment_delete/{comment_id}")
async def delete_comment(comment_id: int):
    result = delete_comment_db(comment_id)
    if result:
        return {"status": 0, "message": "Комментарий успешно удален"}
    return {"status": 1, "message": "ошибка в удалении комментария"}


@post_router.put("/post_change/{post_id}")
async def change_post(post_id: int, main_text:str):
    result = change_post_db(post_id,main_text)
    if result:
        return {"status": 0, "message": result}
    return {"status": 1, "message": "ошибка в изменения поста"}


@post_router.put("/comment_change/{comment_id}")
async def change_comment(comment_id: int, main_text:str):
    result = change_comment_db(comment_id, main_text)
    if result:
        return {"status": 0, "message": result}
    return {"status": 1, "message": "ошибка в изменении комментария"}
