from fastapi import FastAPI
from database import  engine, Base

app = FastAPI(docs_url="/")
Base.metadata.create_all(bind=engine)


from api.postservice.post_api import post_router
from api.userservice.users_api import user_router
app.include_router(user_router)
app.include_router(post_router)

