from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class UserModel(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    username = Column(String(18), nullable=False,unique= True)
    password = Column(String(18), nullable=False)
    role = Column(String(10), nullable=False)
    status = Column(String(10), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime) 

    # Quan hệ 1-1 với player, developer, designer, admin

    player = relationship("PlayerModel", back_populates="user", uselist=False)
    developer = relationship("DeveloperModel", back_populates="user", uselist=False)
    designer = relationship("DesignerModel", back_populates="user", uselist=False)
    admin = relationship("AdminModel", back_populates="user", uselist=False)
    payouts = relationship("PayoutModel", back_populates="recipient")