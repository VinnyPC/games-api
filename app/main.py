from fastapi import FastAPI

from app.core import config
from app.routes import game

app = FastAPI()

app.include_router(game.router)
