from database import get_db
from database.models import *

def add_post_db(user_id, main_text):
    with next(get_db()) as db:
        new_post = Post(user_id=user_id, main_text=main_text)
        db.add(new_post)
        db.commit()
        return True

def change_post_db(post_id,main_text):
    with next(get_db()) as db:
        post = db.query(Post).filter_by(id=post_id).first()
        if post:
             post.main_text = main_text
             db.commit()
             db.refresh(post)
             return True
        return False

def delete_post_db(post_id):
    with next(get_db()) as db:
        post = db.query(Post).filter_by(id=post_id).first()
        if post:
            db.delete(post)
            db.commit()
            return True
        return False

def add_comment_db(comment_id,user_id, main_text):
    with next(get_db()) as db:
        new_comment = Comment(id=comment_id,user_id=user_id, main_text=main_text)
        db.add(new_comment)
        db.commit()
        return True

def change_comment_db(comment_id, main_text):
    with next(get_db()) as db:
        comment = db.query(Comment).filter_by(id=comment_id).first()
        if comment:
            comment.main_text = main_text
            db.commit()
            db.refresh(comment)
            return True
        return False

def delete_comment_db(comment_id):
    with next(get_db()) as db:
        comment = db.query(Comment).filter_by(id=comment_id).first()
        if comment:
            db.delete(comment)
            db.commit()
            return True
        return False






