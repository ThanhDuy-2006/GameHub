from domain.models.redeem import Redeem
from domain.models.iredeem_repository import IRedeemRepository
from typing import List, Optional

class RedeemService:
    def __init__(self, repository: IRedeemRepository, player_service=None, reward_service=None):
        self.repository = repository
        self.player_service = player_service
        self.reward_service = reward_service

    def create_redeem(self, player_id: int, reward_id: int, points_used: int, status: str, created_at) -> Redeem:
        # Kiểm tra reward có sẵn không
        if self.reward_service and not self.reward_service.check_availability(reward_id, points_used):
            raise ValueError("Reward is not available or insufficient points")
        
        # Tạo redeem record
        redeem = Redeem(id=None, player_id=player_id, reward_id=reward_id, points_used=points_used, status=status, created_at=created_at)
        result = self.repository.add(redeem)
        
        # Trừ points của player
        if self.player_service:
            self.player_service.deduct_point(player_id, points_used)
        
        # Giảm quantity của reward
        if self.reward_service:
            self.reward_service.decrease_quantity(reward_id, 1)
        
        return result

    def get_redeem(self, redeem_id: int) -> Optional[Redeem]:
        return self.repository.get_by_id(redeem_id)

    def list_redeems(self) -> List[Redeem]:
        return self.repository.list()

    def update_redeem(self, redeem_id: int, player_id: int, reward_id: int, points_used: int, status: str, created_at) -> Redeem:
        redeem = Redeem(id=redeem_id, player_id=player_id, reward_id=reward_id, points_used=points_used, status=status, created_at=created_at)
        return self.repository.update(redeem)

    def delete_redeem(self, redeem_id: int) -> None:
        self.repository.delete(redeem_id)