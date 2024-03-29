from sqlalchemy import String, Integer, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.db_config import Base
import uuid
from datetime import datetime


class Otp(Base):
    __tablename__ = "otps"
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id", ondelete="CASCADE"), index=True)
    email = Column(String(36))
    otp = Column(String(6))
    attempts = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship("User")
