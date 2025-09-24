from abc import ABC, abstractmethod
from .redeem import Redeem
from typing import List, Optional

class IRedeemRepository(ABC):
    @abstractmethod
    def add(self, redeem: Redeem) -> Redeem:
        pass

    @abstractmethod
    def get_by_id(self, redeem_id: int) -> Optional[Redeem]:
        pass

    @abstractmethod
    def list(self) -> List[Redeem]:
        pass

    @abstractmethod
    def update(self, redeem: Redeem) -> Redeem:
        pass

    @abstractmethod
    def delete(self, redeem_id: int) -> None:
        pass