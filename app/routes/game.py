from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.repositories.game_repository_db import GameRepositoryDB
from app.schemas.game import GameRead
from app.schemas.game import GameCreate
from app.service.gameService import GameService

router = APIRouter()


def get_service(db: Session = Depends(get_db)):
    repo = GameRepositoryDB(db)
    return GameService(repo)


@router.get("/games")
def list_games(service: GameService = Depends(get_service)):
    return service.list_all()


@router.post("/games")
def create_game(game_data: GameCreate, service: GameService = Depends(get_service)):
    return service.create_game(game_data)
