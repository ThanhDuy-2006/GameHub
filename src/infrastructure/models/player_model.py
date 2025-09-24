from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class PlayerModel(Base):
    __tablename__ = 'player'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, unique=True )
    scores = Column(Integer)
    point = Column(Integer)
    
    user = relationship("UserModel", back_populates="player")
    redeems = relationship("RedeemModel", back_populates="player")
    reviews = relationship("GameReviewModel", back_populates="player")
    leaderboards = relationship("LeaderboardModel", back_populates="player")
