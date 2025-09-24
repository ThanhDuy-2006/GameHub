from abc import ABC, abstractmethod
from .leaderboard import Leaderboard
from typing import List, Optional

class ILeaderboardRepository(ABC):
    @abstractmethod
    def add(self, leaderboard: Leaderboard) -> Leaderboard:
        pass

    @abstractmethod
    def get_by_id(self, leaderboard_id: int) -> Optional[Leaderboard]:
        pass

    @abstractmethod
    def list(self) -> List[Leaderboard]:
        pass

    @abstractmethod
    def get_by_game_id(self, game_id: int) -> List[Leaderboard]:
        pass

    @abstractmethod
    def get_by_player_id(self, player_id: int) -> List[Leaderboard]:
        pass

    @abstractmethod
    def update(self, leaderboard: Leaderboard) -> Leaderboard:
        pass

    @abstractmethod
    def delete(self, leaderboard_id: int) -> None:
        pass