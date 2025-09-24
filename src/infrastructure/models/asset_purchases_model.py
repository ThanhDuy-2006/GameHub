from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from infrastructure.databases.base import Base
from sqlalchemy.orm import relationship
import datetime

class AssetPurchasesModel(Base):
    __tablename__ = 'asset_purchases'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    dev_id = Column(Integer, ForeignKey("developer.id"), nullable=False)
    asset_id = Column(Integer, ForeignKey("asset.id"), nullable=False)
    purchase_date = Column(DateTime, default=datetime.datetime.utcnow)
    amount_paid = Column(Float, nullable=False)

    # Quan hệ
    developer = relationship("DeveloperModel", back_populates="asset_purchases")
    asset = relationship("AssetModel", back_populates="asset_purchases")