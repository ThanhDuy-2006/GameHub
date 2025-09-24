from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base


class PayoutModel(Base):
    __tablename__ = 'payout_transactions'
    __table_args__ = {'extend_existing': True}

    transactions_id = Column(Integer, primary_key=True, autoincrement=True)
    recipient_id = Column(Integer,ForeignKey('user.id'), nullable=False)   # developer.id hoặc designer.id
    recipient_type = Column(String(50), nullable=False)  # 'developer' | 'designer'
    amount = Column(Float, nullable=False)
    transaction_date = Column(DateTime, nullable=False)
    status = Column(String(20), nullable=False)
    processed_by_admin_id = Column(Integer, ForeignKey('admin.id'), nullable=False)

    admin = relationship("AdminModel", back_populates="payout_transactions")
    recipient = relationship("UserModel", back_populates="payouts")
