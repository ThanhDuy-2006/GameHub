from abc import ABC, abstractmethod
from .game_review import GameReview
from typing import List, Optional

class IGameReviewRepository(ABC):
    @abstractmethod
    def add(self, review: GameReview) -> GameReview:
        pass

    @abstractmethod
    def get_by_id(self, review_id: int) -> Optional[GameReview]:
        pass

    @abstractmethod
    def list(self) -> List[GameReview]:
        pass

    @abstractmethod
    def update(self, review: GameReview) -> GameReview:
        pass

    @abstractmethod
    def delete(self, review_id: int) -> None:
        pass
