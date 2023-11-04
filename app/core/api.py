from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect

from starlette import status
from starlette.authentication import requires

from pydantic import BaseModel

from app.core.chat import ConnectionManager


router = APIRouter(tags=["Core Endpoints"])
manager = ConnectionManager()

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
    print(request.user)
    return Feed(posts=[])

@router.websocket('/chat/{user_id}')
@requires('authenticated')
async def chat_socket(websocket: WebSocket, user_id: str):
    await manager.connect(websocket)
    await manager.broadcast(f'Client #{user_id} joins the chat')
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client #{user_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{user_id} left the chat")