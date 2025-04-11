from sqlalchemy.orm import Session
from app.models.game import Game
from app.schemas.game import GameCreate

def create_game(db: Session, product: GameCreate):
    db_game = Game(**product.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game
