from sqlalchemy import Column, Integer, String, DateTime, Boolean , ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from infrastructure.databases.base import Base

class ApiaccessModel(Base):
    __tablename__ = 'apiaccess'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True)
    developer_id = Column(Integer, ForeignKey('developer.id'), nullable=False)
    admin_id = Column(Integer, ForeignKey("admin.id"))
   

    api_type = Column(String(50), nullable=False)   
    api_key = Column(String(128), unique=True)     
    sdk_link = Column(String(255))
    request_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String(30), nullable=False, default="pending")
    
    developer = relationship("DeveloperModel", back_populates="apiaccess")
    admin = relationship("AdminModel", back_populates="apiaccess")