from abc import ABC, abstractmethod
from .asset import Asset
from typing import List, Optional

class IAssetRepository(ABC):
    @abstractmethod
    def add(self, asset: Asset) -> Asset:
        pass

    @abstractmethod
    def get_by_id(self, asset_id: int) -> Optional[Asset]:
        pass

    @abstractmethod
    def list(self) -> List[Asset]:
        pass

    @abstractmethod
    def update(self, asset: Asset) -> Asset:
        pass

    @abstractmethod
    def delete(self, asset_id: int) -> None:
        pass 