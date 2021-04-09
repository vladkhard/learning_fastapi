from fastapi import FastAPI

from db import db
from models import User
from tools import generate_id


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = User.parse_obj(db.users.find_one(user_id))
    return user.dict(skip_defaults=True)

@app.post("/users")
async def post_user(user: User):
    user_data = user.dict()
    user_data["_id"] = generate_id()
    db.users.insert_one(user_data)
    return user_data
