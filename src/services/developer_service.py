from typing import List, Optional
from domain.models.developer import Developer
from domain.models.ideveloper_repository import IDeveloperRepository

class DeveloperService:
    def __init__(self, developer_repository: IDeveloperRepository, user_service=None):
        self.developer_repository = developer_repository
        self.user_service = user_service
    
    def add_developer(self, user_id: int, payment_info: str) -> Developer:
        developer = Developer(
            id=None,
            user_id=user_id,
            payment_info=payment_info
        )
        result = self.developer_repository.add(developer)
        # Cập nhật role của user thành 'developer'
        if self.user_service:
            self.user_service.update_user_role(user_id, 'developer')
        return result
    
    def get_developer_by_id(self, developer_id: int) -> Optional[Developer]:
        return self.developer_repository.get_by_id(developer_id)
    
    def list_developers(self) -> List[Developer]:
        return self.developer_repository.list()
    
    def update_developer(self, developer_id: int, user_id: int, payment_info: str) -> Developer:
        developer = Developer(
            id=developer_id,
            user_id=user_id,
            payment_info=payment_info
        )
        return self.developer_repository.update(developer)
    
    def delete_developer(self, developer_id: int) -> None:
        self.developer_repository.delete(developer_id)

    def get_developer_by_user_id(self, user_id: int) -> Optional[Developer]:
        return self.developer_repository.get_developer_by_user_id(user_id)
