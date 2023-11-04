from fastapi import APIRouter, Request

from starlette import status
from starlette.authentication import requires

from pydantic import BaseModel


router = APIRouter(tags=["Core Endpoints"])

class UserCreate(BaseModel):
    firebase_uid: str

class User(BaseModel):
    id: int
    display_name: str

class Post(BaseModel):
    post_id: int

class Feed(BaseModel):
    posts: list[Post]


@router.get("/healthcheck", status_code=status.HTTP_200_OK)
async def healthcheck(request: Request) -> dict:
    return {"version": request.app.version}

@router.post("/signup", response_model=User)
async def signup(user: UserCreate):
    print(user.firebase_uid)
    return User(id=1, display_name="Omar")

@router.get("/feed", response_model=Feed)
@requires('authenticated')
async def get_feed(request: Request):
    print(request.auth)
    return Feed(posts=[])
