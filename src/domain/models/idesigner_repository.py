from abc import ABC, abstractmethod
from .designer import Designer
from typing import List, Optional

class IDesignerRepository(ABC):
    @abstractmethod
    def add(self, designer: Designer) -> Designer:
        pass

    @abstractmethod
    def get_by_id(self, designer_id: int) -> Optional[Designer]:
        pass

    @abstractmethod
    def list(self) -> List[Designer]:
        pass

    @abstractmethod
    def update(self, designer: Designer) -> Designer:
        pass

    @abstractmethod
    def delete(self, designer_id: int) -> None:
        pass 