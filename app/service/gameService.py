from app.repositories.game_repository_interface import GameRepository
from app.schemas.game import GameUpdate


class GameService:
    def __init__(self, repo: GameRepository):
        self.repo = repo

    def list_all(self):
        return self.repo.get_all()

    def get_by_id(self, game_id: int):
        return self.repo.get_by_id(game_id)

    def create_game(self, game_data):
        return self.repo.create(game_data)

    def update_game(self, game_id: int, game_data: GameUpdate) -> bool:
        return self.repo.update(game_id, game_data)

    def delete_game(self, game_id: int) -> bool:
        return self.repo.delete(game_id)
