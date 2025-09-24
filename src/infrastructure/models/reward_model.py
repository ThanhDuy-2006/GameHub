from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class RewardModel(Base):
    __tablename__ = 'reward'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    point_required = Column(Integer)
    quantity = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    redeems = relationship("RedeemModel", back_populates="reward") 