from domain.models.ireward_repository import IRewardRepository
from domain.models.reward import Reward
from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.models.reward_model import RewardModel
from infrastructure.databases.mssql import session

class RewardRepository(IRewardRepository):
    def __init__(self, session: Session = session):
        self.session = session
        self._rewards = []
        self._id_counter = 1

    def add(self, reward: Reward) -> RewardModel:
        try:
            #Manual mapping from Reward to RewardModel
            reward_model = RewardModel(
                name=reward.name,
                description=reward.description,
                point_required=reward.point_required,
                quantity=reward.quantity,
                created_at=reward.created_at,
                updated_at=reward.updated_at
            )
            self.session.add(reward_model)
            self.session.commit()
            self.session.refresh(reward_model)
            return reward_model
        except Exception as e:
            self.session.rollback()
            raise ValueError('Reward creation failed')
        finally:
            pass

    def get_by_id(self, reward_id: int) -> Optional[RewardModel]:
        return self.session.query(RewardModel).filter_by(id=reward_id).first()

    def list(self) -> List[RewardModel]:
        self._rewards = session.query(RewardModel).all()
        return self._rewards

    def update(self, reward: Reward) -> RewardModel:
        try:
            #Manual mapping from Reward to RewardModel
            reward_model = RewardModel(
                id=reward.id,
                name=reward.name,
                description=reward.description,
                point_required=reward.point_required,
                quantity=reward.quantity,
                created_at=reward.created_at,
                updated_at=reward.updated_at
            )
            self.session.merge(reward_model)
            self.session.commit()
            return reward_model
        except Exception as e:
            self.session.rollback()
            raise ValueError('Reward update failed')
        finally:
            pass

    def delete(self, reward_id: int) -> None:
        try:
            reward = self.session.query(RewardModel).filter_by(id=reward_id).first()
            if reward:
                self.session.delete(reward)
                self.session.commit()
            else:
                raise ValueError('Reward not found')
        except Exception as e:
            self.session.rollback()
            raise ValueError('Reward not found')
        finally:
            pass