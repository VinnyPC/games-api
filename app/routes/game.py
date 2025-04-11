from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.game import GameCreate, GameRead
from app.crud.game import create_game

router = APIRouter()

@router.post("/games/", response_model=GameRead)
def create(game: GameCreate, db: Session = Depends(get_db)):
    return create_game(db, game)
