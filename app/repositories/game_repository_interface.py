from abc import ABC, abstractmethod
from typing import List
from app.schemas.game import GameCreate, GameRead


class GameRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[GameRead]:
        pass

    @abstractmethod
    def get_by_id(self, game_id: int) -> GameRead:
        pass

    @abstractmethod
    def create(self, game: GameCreate) -> GameRead:
        pass