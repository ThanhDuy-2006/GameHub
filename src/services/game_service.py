from infrastructure.repositories.game_repository import GameRepository

class GameService:
    def __init__(self, game_repository: GameRepository):
        self.game_repository = game_repository

    def list_games(self):
        """Get all games"""
        return self.game_repository.list_games()

    def get_game(self, game_id):
        """Get a game by id"""
        return self.game_repository.get_game(game_id)

    def create_game(self, dev_id, name, description, price, sources, created_at, updated_at):
        """Create a new game"""
        return self.game_repository.create_game(
            dev_id=dev_id,
            name=name,
            description=description,
            price=price,
            sources=sources,
            created_at=created_at,
            updated_at=updated_at
        )

    def update_game(self, game_id, dev_id, name, description, price, sources, created_at, updated_at):
        """Update a game by id"""
        return self.game_repository.update_game(
            game_id=game_id,
            dev_id=dev_id,
            name=name,
            description=description,
            price=price,
            sources=sources,
            created_at=created_at,
            updated_at=updated_at
        )

    def delete_game(self, game_id):
        """Delete a game by id"""
        return self.game_repository.delete_game(game_id)
