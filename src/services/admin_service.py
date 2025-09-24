from domain.models.admin import Admin
from domain.models.iadmin_repository import IAdminRepository
from typing import List, Optional

class AdminService:
    def __init__(self, repository: IAdminRepository, user_service=None):
        self.repository = repository
        self.user_service = user_service

    def create_admin(self, user_id: int) -> Admin:
        admin = Admin(id=None, user_id=user_id)
        result = self.repository.add(admin)
        
        # Cập nhật role của user thành 'admin'
        if self.user_service:
            self.user_service.update_user_role(user_id, 'admin')
        
        return result

    def get_admin(self, admin_id: int) -> Optional[Admin]:
        return self.repository.get_by_id(admin_id)

    def list_admins(self) -> List[Admin]:
        return self.repository.list()

    def update_admin(self, admin_id: int, user_id: int) -> Admin:
        admin = Admin(id=admin_id, user_id=user_id)
        return self.repository.update(admin)

    def delete_admin(self, admin_id: int) -> None:
        self.repository.delete(admin_id)

    def get_admin_by_user_id(self, user_id):
        return self.repository.get_admin_by_user_id(user_id)