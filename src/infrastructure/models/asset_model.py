from sqlalchemy import Column, Integer, String, DateTime, Boolean , ForeignKey, Numeric
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class AssetModel(Base):
    __tablename__ = 'asset'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    designer_id = Column(Integer, ForeignKey('designer.id'), nullable=False)
    name = Column(String(255), nullable=False)
    type = Column(String(50))
    price = Column(Numeric(10, 2), nullable=False, default=0)
    download_count = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    designer = relationship("DesignerModel", back_populates="assets")
    asset_purchases = relationship("AssetPurchasesModel", back_populates="asset")
