from sqlalchemy.orm import Session
from app.models.game import Game as GameModel
from app.schemas.game import GameCreate
from app.repositories.game_repository_interface import GameRepository


class GameRepositoryDB(GameRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(GameModel).all()

    def get_by_id(self, game_id: int):
        return self.db.query(GameModel).filter(GameModel.id == game_id).first()

    def create(self, game: GameCreate):
        db_game = GameModel(**game.dict())
        self.db.add(db_game)
        self.db.commit()
        self.db.refresh(db_game)
        return db_game
