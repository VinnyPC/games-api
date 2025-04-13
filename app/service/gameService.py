from app.repositories.game_repository_interface import GameRepository


class GameService:
    def __init__(self, repo: GameRepository):
        self.repo = repo

    def list_all(self):
        return self.repo.get_all()

    def get_one(self, game_id: int):
        return self.repo.get_by_id(game_id)

    def create_game(self, game_data):
        return self.repo.create(game_data)
