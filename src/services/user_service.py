from typing import List, Optional
from domain.models.user import User
from domain.models.iuser_repository import IUserRepository


class UserService:
    def __init__(self, user_repository: IUserRepository, player_service=None, admin_service=None, developer_service=None, designer_service=None):
        self.user_repository = user_repository
        self.player_service = player_service
        self.admin_service = admin_service
        self.developer_service = developer_service
        self.designer_service = designer_service
    
    def add_user(self, username: str, password: str, role: str, status: str, created_at, updated_at) -> User:
        user = User(id=None, username=username, password=password, role=role, status=status, created_at=created_at, updated_at=updated_at)
        return self.user_repository.add(user)
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.user_repository.get_by_id(user_id)
    
    def list_users(self) -> List[User]:
        return self.user_repository.list()
    
    def update_user(self, user_id: int, username: str, password: str, role: str, status: str, created_at, updated_at) -> User:
        return self.user_repository.update(user_id, username, password, role, status, updated_at)
    
    def delete_user(self, user_id: int) -> None:
        self.user_repository.delete(user_id)
    
    def update_user_role(self, user_id: int, role: str) -> None:
        """Cập nhật role của user"""
        user = self.user_repository.get_by_id(user_id)
        if user:
            # Cập nhật user với role mới, giữ nguyên các field khác
            from datetime import datetime
            self.user_repository.update(
                user_id=user_id,
                username=user.username,
                password=user.password,
                role=role,  # Role mới
                status=user.status,
                updated_at=datetime.utcnow()
            )
        else:
            raise ValueError(f'User with id {user_id} not found')
    
    def authenticate(self, username: str, password: str) -> Optional[User]:
        user = self.user_repository.get_by_username(username)
        if user and user.password == password:
            return user
        return None
    
    def create_role_data(self, role, user_id, **kwargs):
        """
        Insert user data into the corresponding role table
        """
        if role == 'player' and self.player_service:
            scores = kwargs.get('scores', 0)
            point = kwargs.get('point', 0)
            from datetime import datetime
            self.player_service.create_player(user_id, scores, point, datetime.utcnow(), datetime.utcnow())
        elif role == 'admin' and self.admin_service:
            self.admin_service.create_admin(user_id)
        elif role == 'developer' and self.developer_service:
            payment_info = kwargs.get('payment_info', '')
            self.developer_service.add_developer(user_id, payment_info)
        elif role == 'designer' and self.designer_service:
            paymentinfo = kwargs.get('paymentinfo', '')
            self.designer_service.add_designer(user_id, paymentinfo)
        else:
            # Nếu không có service phù hợp, fallback gọi repository
            self.user_repository.insert_role_data(role, user_id)
    
    def sync_role_tables(self):
        """
        Sync user data to corresponding role tables for all users
        """
        users = self.list_users()
        for user in users:
            self.create_role_data(user.role, user.id)