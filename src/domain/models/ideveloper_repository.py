from abc import ABC, abstractmethod
from .developer import Developer
from typing import List, Optional

class IDeveloperRepository(ABC):
    @abstractmethod
    def add(self, developer: Developer) -> Developer:
        pass

    @abstractmethod
    def get_by_id(self, developer_id: int) -> Optional[Developer]:
        pass

    @abstractmethod
    def list(self) -> List[Developer]:
        pass

    @abstractmethod
    def update(self, developer: Developer) -> Developer:
        pass

    @abstractmethod
    def delete(self, developer_id: int) -> None:
        pass