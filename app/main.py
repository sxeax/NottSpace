from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.auth import auth_middleware

from app.core.log import logger
from app.core.api import router as core_router

app = FastAPI(middleware=auth_middleware)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(core_router)

logger.info("App is ready!")
