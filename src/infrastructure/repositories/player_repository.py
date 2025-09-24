from domain.models.iplayer_repository import IPlayerRepository
from domain.models.player import Player
from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.models.player_model import PlayerModel
from infrastructure.databases.mssql import session

class PlayerRepository(IPlayerRepository):
    def __init__(self, session: Session = session):
        self.session = session
        self._players = []
        self._id_counter = 1

    def add(self, player: Player) -> PlayerModel:
        try:
            #Manual mapping from Player to PlayerModel
            player_model = PlayerModel(
                user_id=player.user_id,
                scores=player.scores,
                point=player.point,  # Note: PlayerModel uses 'point'
            )
            self.session.add(player_model)
            self.session.commit()
            self.session.refresh(player_model)
            return player_model
        except Exception as e:
            self.session.rollback()
            raise ValueError('Player creation failed')
        finally:
            self.session.close()

    def get_by_id(self, player_id: int) -> Optional[PlayerModel]:
        return self.session.query(PlayerModel).filter_by(id=player_id).first()

    def list(self) -> List[PlayerModel]:
        self._players = session.query(PlayerModel).all()
        return self._players

    def update(self, player: Player) -> PlayerModel:
        try:
            #Manual mapping from Player to PlayerModel
            player_model = PlayerModel(
                id=player.id,
                user_id=player.user_id,
                scores=player.scores,
                point=player.point,  # Note: PlayerModel uses 'point'
            )
            self.session.merge(player_model)
            self.session.commit()
            return player_model
        except Exception as e:
            self.session.rollback()
            raise ValueError('Player update failed')
        finally:
            self.session.close()


    def delete(self, player_id: int) -> None:
        try:
            player = self.session.query(PlayerModel).filter_by(id=player_id).first()
            if player:
                self.session.delete(player)
                self.session.commit()
            else:
                raise ValueError('Player not found')
        except Exception as e:
            self.session.rollback()
            raise ValueError('Player not found')
        finally:
            self.session.close()

    def get_player_by_user_id(self, user_id):
        return self.session.query(PlayerModel).filter_by(user_id=user_id).first()
