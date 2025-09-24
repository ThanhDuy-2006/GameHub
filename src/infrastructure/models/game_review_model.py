from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class GameReviewModel(Base):
    __tablename__ = 'game_review'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'), nullable=False)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)  
    rating = Column(Integer, nullable=False)
    comment = Column(String(500), nullable=True)
    review_date = Column(DateTime)

    game = relationship("GameModel", back_populates="reviews")
    player = relationship("PlayerModel", back_populates="reviews")