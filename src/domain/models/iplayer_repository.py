from abc import ABC, abstractmethod
from .player import Player
from typing import List, Optional

class IPlayerRepository(ABC):
    @abstractmethod
    def add(self, user: Player) -> Player:
        pass

    @abstractmethod
    def get_by_id(self, player_id: int) -> Optional[Player]:
        pass

    @abstractmethod
    def list(self) -> List[Player]:
        pass

    @abstractmethod
    def update(self, user: Player) -> Player:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass 