from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base


class AdminModel(Base):
    __tablename__ = 'admin'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True)

    user = relationship('UserModel', back_populates='admin')
    payout_transactions = relationship('PayoutModel', back_populates='admin')
    apiaccess = relationship("ApiaccessModel", back_populates="admin")
