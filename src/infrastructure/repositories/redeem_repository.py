from domain.models.iredeem_repository import IRedeemRepository
from domain.models.redeem import Redeem
from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.models.redeem_model import RedeemModel
from infrastructure.databases.mssql import session

class RedeemRepository(IRedeemRepository):
    def __init__(self, session: Session = session):
        self.session = session
        self._redeems = []
        self._id_counter = 1

    def add(self, redeem: Redeem) -> RedeemModel:
        try:
            #Manual mapping from Redeem to RedeemModel
            redeem_model = RedeemModel(
                player_id=redeem.player_id,
                reward_id=redeem.reward_id,
                points_used=redeem.points_used,
                status=redeem.status,
                created_at=redeem.created_at
            )
            self.session.add(redeem_model)
            self.session.commit()
            self.session.refresh(redeem_model)
            return redeem_model
        except Exception as e:
            self.session.rollback()
            raise ValueError('Redeem creation failed')
        finally:
            self.session.close()

    def get_by_id(self, redeem_id: int) -> Optional[RedeemModel]:
        return self.session.query(RedeemModel).filter_by(id=redeem_id).first()

    def list(self) -> List[RedeemModel]:
        self._redeems = session.query(RedeemModel).all()
        return self._redeems

    def update(self, redeem: Redeem) -> RedeemModel:
        try:
            #Manual mapping from Redeem to RedeemModel
            redeem_model = RedeemModel(
                id=redeem.id,
                player_id=redeem.player_id,
                reward_id=redeem.reward_id,
                points_used=redeem.points_used,
                status=redeem.status,
                created_at=redeem.created_at
            )
            self.session.merge(redeem_model)
            self.session.commit()
            return redeem_model
        except Exception as e:
            self.session.rollback()
            raise ValueError('Redeem update failed')
        finally:
            self.session.close()

    def delete(self, redeem_id: int) -> None:
        try:
            redeem = self.session.query(RedeemModel).filter_by(id=redeem_id).first()
            if redeem:
                self.session.delete(redeem)
                self.session.commit()
            else:
                raise ValueError('Redeem not found')
        except Exception as e:
            self.session.rollback()
            raise ValueError('Redeem not found')
        finally:
            self.session.close()