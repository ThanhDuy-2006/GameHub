from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class RedeemModel(Base):
    __tablename__ = 'redeem'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'))
    reward_id = Column(Integer, ForeignKey('reward.id'))
    points_used = Column(Integer)
    status = Column(String)
    created_at = Column(DateTime)
    
    player = relationship("PlayerModel", back_populates="redeems")
    reward = relationship("RewardModel", back_populates="redeems")