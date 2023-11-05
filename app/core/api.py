from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from starlette import status
from starlette.authentication import requires
from pydantic import BaseModel
from app.core.chat import ConnectionManager
from app.db import queries


router = APIRouter(tags=["Core Endpoints"])
manager = ConnectionManager()

class UserCreate(BaseModel):
    firebase_uid: str
    display_name: str

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

@router.post("/signup", status_code=200)
async def signup(user: UserCreate):
    user = queries.create_user(
        firebase_uid=user.firebase_uid,
        display_name=user.display_name
    )
    return {}

@router.get('/friend_count')
@requires('authenticated')
async def get_friend_count(request: Request):
    print(request.user)
    return {'friend_count': 4}

@router.get("/feed", response_model=Feed)
@requires('authenticated')
async def get_feed(request: Request):
    print(request.user)
    return Feed(posts=[])

x = 2
@router.get('/get_data')
@requires('authenticated')
async def get_data(request: Request):
    user = queries.get_user(firebase_uid=request.user)
    friends = list(queries.get_friends(user_id=user['user_id']))
    return {
        'no_friends': len(friends),
        'display_name': user['display_name'],
        'created_at': user['created_at'],
    }

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

