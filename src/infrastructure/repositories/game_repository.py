from infrastructure.models.game_model import GameModel

class GameRepository:
    def __init__(self, session):
        self.session = session

    def list_games(self):
        """Get all games"""
        return self.session.query(GameModel).all()

    def get_game(self, game_id):
        """Get a game by id"""
        return self.session.query(GameModel).filter(GameModel.id == game_id).first()

    def create_game(self, dev_id, name, description, price, sources, created_at, updated_at):
        """Create a new game"""
        game = GameModel(
            dev_id=dev_id,
            name=name,
            description=description,
            price=price,
            sources=sources,
            created_at=created_at,
            updated_at=updated_at
        )
        self.session.add(game)
        self.session.commit()
        return game

    def update_game(self, game_id, dev_id, name, description, price, sources, created_at, updated_at):
        """Update a game by id"""
        game = self.get_game(game_id)
        if game:
            game.dev_id = dev_id
            game.name = name
            game.description = description
            game.price = price
            game.sources = sources
            game.created_at = created_at
            game.updated_at = updated_at
            self.session.commit()
        return game

    def delete_game(self, game_id):
        """Delete a game by id"""
        game = self.get_game(game_id)
        if game:
            self.session.delete(game)
            self.session.commit()
            return True
        return False
