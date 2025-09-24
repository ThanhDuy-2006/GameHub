from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class TodoModel(Base):
    __tablename__ = 'todo'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(String, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)