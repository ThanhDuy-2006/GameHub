from domain.models.leaderboard import Leaderboard
from domain.models.ileaderboard_repository import ILeaderboardRepository
from typing import List, Optional

class LeaderboardService:
    def __init__(self, repository: ILeaderboardRepository):
        self.repository = repository

    def create_leaderboard_entry(self, player_id: int, game_id: int, score: int, achieved_at) -> Leaderboard:
        leaderboard = Leaderboard(id=None, player_id=player_id, game_id=game_id, score=score, achieved_at=achieved_at)
        return self.repository.add(leaderboard)

    def get_leaderboard_entry(self, leaderboard_id: int) -> Optional[Leaderboard]:
        return self.repository.get_by_id(leaderboard_id)

    def list_leaderboard_entries(self) -> List[Leaderboard]:
        return self.repository.list()

    def get_leaderboard_by_game(self, game_id: int) -> List[Leaderboard]:
        return self.repository.get_by_game_id(game_id)

    def get_leaderboard_by_player(self, player_id: int) -> List[Leaderboard]:
        return self.repository.get_by_player_id(player_id)

    def update_leaderboard_entry(self, leaderboard_id: int, player_id: int, game_id: int, score: int, achieved_at) -> Leaderboard:
        leaderboard = Leaderboard(id=leaderboard_id, player_id=player_id, game_id=game_id, score=score, achieved_at=achieved_at)
        return self.repository.update(leaderboard)

    def delete_leaderboard_entry(self, leaderboard_id: int) -> None:
        self.repository.delete(leaderboard_id)