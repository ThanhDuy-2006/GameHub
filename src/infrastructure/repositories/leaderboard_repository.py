from domain.models.ileaderboard_repository import ILeaderboardRepository
from domain.models.leaderboard import Leaderboard
from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.models.leaderboard_model import LeaderboardModel
from infrastructure.databases.mssql import session

class LeaderboardRepository(ILeaderboardRepository):
    def __init__(self, session: Session = session):
        self.session = session
        self._leaderboards = []
        self._id_counter = 1

    def add(self, leaderboard: Leaderboard) -> LeaderboardModel:
        try:
            # Manual mapping from Leaderboard to LeaderboardModel
            leaderboard_model = LeaderboardModel(
                player_id=leaderboard.player_id,
                game_id=leaderboard.game_id,
                score=leaderboard.score,
                achieved_at=leaderboard.achieved_at
            )
            self.session.add(leaderboard_model)
            self.session.commit()
            self.session.refresh(leaderboard_model)
            return leaderboard_model
        except Exception as e:
            self.session.rollback()
            raise ValueError('Failed to create leaderboard entry')
        finally:
            pass

    def get_by_id(self, leaderboard_id: int) -> Optional[LeaderboardModel]:
        return self.session.query(LeaderboardModel).filter_by(id=leaderboard_id).first()

    def list(self) -> List[LeaderboardModel]:
        self._leaderboards = session.query(LeaderboardModel).all()
        return self._leaderboards

    def get_by_game_id(self, game_id: int) -> List[LeaderboardModel]:
        return self.session.query(LeaderboardModel).filter_by(game_id=game_id).order_by(LeaderboardModel.score.desc()).all()

    def get_by_player_id(self, player_id: int) -> List[LeaderboardModel]:
        return self.session.query(LeaderboardModel).filter_by(player_id=player_id).all()

    def update(self, leaderboard: LeaderboardModel) -> LeaderboardModel:
        try:
            # Manual mapping from Leaderboard to LeaderboardModel
            leaderboard_model = LeaderboardModel(
                id=leaderboard.id,
                player_id=leaderboard.player_id,
                game_id=leaderboard.game_id,
                score=leaderboard.score,
                achieved_at=leaderboard.achieved_at
            )
            self.session.merge(leaderboard_model)
            self.session.commit()
            return leaderboard_model
        except Exception as e:
            self.session.rollback()
            raise ValueError('Leaderboard entry not found')
        finally:
            pass

    def delete(self, leaderboard_id: int) -> None:
        try:
            leaderboard = self.session.query(LeaderboardModel).filter_by(id=leaderboard_id).first()
            if leaderboard:
                self.session.delete(leaderboard)
                self.session.commit()
            else:
                raise ValueError('Leaderboard entry not found')
        except Exception as e:
            self.session.rollback()
            raise ValueError('Leaderboard entry not found')
        finally:
            pass