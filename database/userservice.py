from database import get_db
from database.models import *

def check_username(username:str):
    db = next(get_db())
    checker = db.query(User).filter_by(username=username).first()
    if checker:
        return True
    return False


def check_email(email:str):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()
    if checker:
        return True
    return False

def registration_db(username:str, email:str,password:str, country:str=None, birthday:str=None):
    db = next(get_db())
    if check_username(username):
        return "Такое имя пользователя занято, попробуйте новый."
    if check_email(email):
        return "Email занят!"
    new_user = User(username=username, email=email, password=password, country=country, birthday=birthday)
    db.add(new_user)
    db.commit()
    return True

def login_db(identificator, password):
    with next(get_db()) as db:
        user = db.query(User).filter_by(username=identificator).first()
        if not user:
            user = db.query(User).filter_by(email=identificator).first()
        if user and user.password == password:
            return {"status": 1, "message": user.id}
        return {"status": 0, "message": "Ошибка, убедитесь,что правильно вели ваши данные!"}


