from domain.models.game_review import GameReview
from domain.models.igame_review_repository import IGameReviewRepository
from typing import List, Optional

class GameReviewService:
    def __init__(self, repository: IGameReviewRepository):
        self.repository = repository

    def create_review(self, game_id: int, player_id: int, rating: int, comment: str | None, review_date) -> GameReview:
        review = GameReview(id=None, game_id=game_id, player_id=player_id, rating=rating, comment=comment, review_date=review_date)
        return self.repository.add(review)

    def get_review(self, review_id: int) -> Optional[GameReview]:
        return self.repository.get_by_id(review_id)

    def list_reviews(self) -> List[GameReview]:
        return self.repository.list()

    def update_review(self, review_id: int, game_id: int, player_id: int, rating: int, comment: str | None, review_date) -> GameReview:
        review = GameReview(id=review_id, game_id=game_id, player_id=player_id, rating=rating, comment=comment, review_date=review_date)
        return self.repository.update(review)

    def delete_review(self, review_id: int) -> None:
        self.repository.delete(review_id)
