from domain.models.igame_review_repository import IGameReviewRepository
from domain.models.game_review import GameReview
from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.models.game_review_model import GameReviewModel
from infrastructure.databases.mssql import session

class GameReviewRepository(IGameReviewRepository):
    def __init__(self, session: Session = session):
        self.session = session

    def add(self, review: GameReview) -> GameReviewModel:
        try:
            model = GameReviewModel(
                game_id=review.game_id,
                player_id=review.player_id,
                rating=review.rating,
                comment=review.comment,
                review_date=review.review_date,
            )
            self.session.add(model)
            self.session.commit()
            self.session.refresh(model)
            return model
        except Exception:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def get_by_id(self, review_id: int) -> Optional[GameReviewModel]:
        return self.session.query(GameReviewModel).filter_by(id=review_id).first()

    def list(self) -> List[GameReviewModel]:
        return self.session.query(GameReviewModel).all()

    def update(self, review: GameReview) -> GameReviewModel:
        try:
            model = GameReviewModel(
                id=review.id,
                game_id=review.game_id,
                player_id=review.player_id,
                rating=review.rating,
                comment=review.comment,
                review_date=review.review_date,
            )
            self.session.merge(model)
            self.session.commit()
            return model
        except Exception as e:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def delete(self, review_id: int) -> None:
        try:
            model = self.session.query(GameReviewModel).filter_by(id=review_id).first()
            if model:
                self.session.delete(model)
                self.session.commit()
            else:
                raise ValueError('GameReview not found')
        except Exception:
            self.session.rollback()
            raise
        finally:
            self.session.close()
