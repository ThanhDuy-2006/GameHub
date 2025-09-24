from abc import ABC, abstractmethod
from .asset_purchases import Asset_Purchase
from typing import List, Optional

class IAssetRepository(ABC):
    @abstractmethod
    def add(self, asset: Asset_Purchase) -> Asset_Purchase:
        pass

    @abstractmethod
    def get_by_id(self, asset_id: int) -> Optional[Asset_Purchase]:
        pass

    @abstractmethod
    def list(self) -> List[Asset_Purchase]:
        pass

    @abstractmethod
    def update(self, asset: Asset_Purchase) -> Asset_Purchase:
        pass

    @abstractmethod
    def delete(self, asset_id: int) -> None:
        pass