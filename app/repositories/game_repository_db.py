from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.game import Game as GameModel
from app.schemas.game import GameCreate, GameUpdate
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

    def update(self, game_id: int, game_data: GameUpdate) -> bool:
        game = self.db.query(GameModel).filter(GameModel.id == game_id).first()

        if not game:
            raise ValueError("Game não encontrado, verique o id")

        game.name = game_data.name
        game.description = game_data.description
        game.price = game_data.price
        game.gender = game_data.gender
        game.progress = game_data.progress

        self.db.commit()
        self.db.refresh(game)
        return game

    def delete(self, game_id: int):
        game = self.db.query(GameModel).filter(GameModel.id == game_id).first()

        if not game:
            raise ValueError("Game não encontrado, verique o id")

        self.db.delete(game)

        self.db.commit()


