from sqlalchemy import Column, Integer, String, DateTime, Boolean , ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class DesignerModel(Base):
    __tablename__ = 'designer'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    paymentinfo = Column(String(255), nullable=True)



 #các mối quan hệ
    assets = relationship("AssetModel", back_populates="designer")
    user = relationship("UserModel", back_populates="designer")


