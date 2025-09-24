from abc import ABC, abstractmethod
from .admin import Admin
from typing import List, Optional

class IAdminRepository(ABC):
    @abstractmethod
    def add(self, admin: Admin) -> Admin:
        pass

    @abstractmethod
    def get_by_id(self, admin_id: int) -> Optional[Admin]:
        pass

    @abstractmethod
    def list(self) -> List[Admin]:
        pass

    @abstractmethod
    def update(self, admin: Admin) -> Admin:
        pass

    @abstractmethod
    def delete(self, admin_id: int) -> None:
        pass