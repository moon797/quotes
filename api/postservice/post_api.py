from fastapi import APIRouter, HTTPException
from database.postservice import *

post_router = APIRouter(tags=["Управление пользователями"], prefix="/user")


@post_router.post("/post")
async def add_post(user_id:int, main_text:str):
    result = add_post_db(user_id=user_id, main_text=main_text)
    if result:
        return {"status": 0, "message": result}
    raise HTTPException(status_code=400, detail="Ошибка, попробуйте заново!")


@post_router.post("/comment")
async def add_comment(comment_id:int, user_id:int, main_text:str):
    result = add_comment_db(user_id=user_id, comment_id=comment_id, main_text=main_text)
    if result:
        return {"status": 0, "message": result}
    raise HTTPException(status_code=400, detail="Ошибка, убедитесь, что вы правильно ввели все данные")

@post_router.delete("/post_delete/{post_id}")
async def remove_post(post_id: int):
    result = delete_post_db(post_id)
    if result:
        return {"status": 0, "message": "Пост успешно удален"}
    raise HTTPException(status_code=404, detail="Пост не найден")


@post_router.delete("/comment_delete/{comment_id}")
async def delete_comment(comment_id: int):
    result = delete_comment_db(comment_id)
    if result:
        return {"status": 0, "message": "Комментарий успешно удален"}
    raise HTTPException(status_code=404, detail="Комментарий не найден")


@post_router.put("/post_change/{post_id}")
async def change_post(post_id: int, main_text:str):
    result = change_post_db(post_id=post_id,main_text=main_text)
    if result:
        return {"status": 0, "message": "Пост успешно изменен"}
    raise HTTPException(status_code=404, detail="Пост не найден")



@post_router.put("/comment_change/{comment_id}")
async def change_comment(comment_id: int, main_text:str):
    result = change_comment_db(comment_id= comment_id, main_text=main_text)
    if result:
        return {"status": 0, "message": "Комментарий успешно изменен"}
    raise HTTPException(status_code=404, detail="Комментарий не найден")