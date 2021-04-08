from fastapi import FastAPI

from models import User, DEFAULT_USER


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/default-user")
async def default_user():
    user = User.parse_obj(DEFAULT_USER)
    return user.dict(skip_defaults=True)
