from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import service
from app.database.connection import get_db
from app.repositories.game_repository_db import GameRepositoryDB
from app.schemas.game import GameUpdate
from app.schemas.game import GameCreate
from app.service.gameService import GameService

router = APIRouter()


def get_service(db: Session = Depends(get_db)):
    repo = GameRepositoryDB(db)
    return GameService(repo)


@router.get("/games")
def list_games(service: GameService = Depends(get_service)):
    return service.list_all()


@router.get("/games/{game_id}")
def get_game(game_id: int, service: GameService = Depends(get_service)):
    return service.get_by_id(game_id)


@router.post("/games")
def create_game(game_data: GameCreate, service: GameService = Depends(get_service)):
    return service.create_game(game_data)


@router.put("/games/{game_id}")
def update_game(game_id: int, game_data: GameUpdate, service: GameService = Depends(get_service)):
    updated = service.update_game(game_id, game_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Game not found")
    return {"message": "Game updated successfully"}


@router.delete("/games/{game_id}")
def delete_game(game_id: int, service: GameService = Depends(get_service)):
    game = service.get_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    service.delete_game(game_id)
    return {"message": "Game deleted successfully"}
