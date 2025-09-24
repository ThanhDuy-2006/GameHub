from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class GameModel(Base):
    __tablename__ = 'game'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    dev_id = Column(Integer, ForeignKey('developer.id'), nullable=False)  
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    sources = Column(String(255), nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    developer = relationship("DeveloperModel", back_populates="games")
    leaderboards = relationship("LeaderboardModel", back_populates="game")
    reviews = relationship("GameReviewModel", back_populates="game")

    

