from sqlalchemy import Column, Integer, String, ForeignKey
from infrastructure.databases.base import Base
from sqlalchemy.orm import relationship

class DeveloperModel(Base):
    __tablename__ = "developer"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)  # liên kết với user
    payment_info = Column(String(50), unique=True)

    # Quan hệ: mỗi dev thuộc 1 user, có thể có nhiều assets và games
    user = relationship("UserModel", back_populates="developer")
    apiaccess = relationship("ApiaccessModel", back_populates="developer")
    games = relationship("GameModel", back_populates="developer")
    asset_purchases = relationship("AssetPurchasesModel", back_populates="developer")