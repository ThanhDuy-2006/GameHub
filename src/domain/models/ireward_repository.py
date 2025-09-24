from abc import ABC, abstractmethod
from .reward import Reward
from typing import List, Optional

class IRewardRepository(ABC):
    @abstractmethod
    def add(self, reward: Reward) -> Reward:
        pass

    @abstractmethod
    def get_by_id(self, reward_id: int) -> Optional[Reward]:
        pass

    @abstractmethod
    def list(self) -> List[Reward]:
        pass

    @abstractmethod
    def update(self, reward: Reward) -> Reward:
        pass

    @abstractmethod
    def delete(self, reward_id: int) -> None:
        pass