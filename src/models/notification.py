from datetime import datetime
import uuid
from sqlalchemy import Column, String,Integer, DateTime, func, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class Notification(Base):
    __tablename__ = "notification"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(CHAR(36), ForeignKey("users.id"), nullable=False)
    notification_message = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    is_read = Column(Enum('unread', 'read', name='notification_status'), default='unread')

    user = relationship("User", back_populates="notifications")