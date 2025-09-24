from typing import List, Optional
from domain.models.designer import Designer
from domain.models.idesigner_repository import IDesignerRepository


class DesignerService:
    def __init__(self, designer_repository: IDesignerRepository, user_service=None):
        self.designer_repository = designer_repository
        self.user_service = user_service
    
    def add_designer(self, user_id: int, paymentinfo: Optional[str]) -> Designer:
        designer = Designer(id=None, user_id=user_id, paymentinfo=paymentinfo)
        result = self.designer_repository.add(designer)
        
        # Cập nhật role của user thành 'designer'
        if self.user_service:
            self.user_service.update_user_role(user_id, 'designer')
        
        return result
    
    def get_designer_by_id(self, designer_id: int) -> Optional[Designer]:
        return self.designer_repository.get_by_id(designer_id)
    
    def list_designers(self) -> List[Designer]:
        return self.designer_repository.list()
    
    def update_designer(self, designer_id: int, user_id: int, paymentinfo: Optional[str]) -> Designer:
        designer = Designer(id=designer_id, user_id=user_id, paymentinfo=paymentinfo)
        return self.designer_repository.update(designer)
    
    def delete_designer(self, designer_id: int) -> None:
        self.designer_repository.delete(designer_id)

    def get_designer_by_user_id(self, user_id: int) -> Optional[Designer]:
        return self.designer_repository.get_designer_by_user_id(user_id)
