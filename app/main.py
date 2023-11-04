from fastapi import FastAPI

from app.core.log import logger
from app.core.api import router as core_router

app = FastAPI()

app.include_router(core_router)

logger.info("App is ready!")
