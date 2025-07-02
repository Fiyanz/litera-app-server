from datetime import datetime
import uuid
from sqlalchemy import Column, String,Integer, DateTime, func, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class Bookmark(Base):
    __tablename__ = "bookmark"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(CHAR(36), nullable=False)  # ForeignKey to User table
    book_id = Column(CHAR(36), nullable=False)  # ForeignKey to Book table
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)

    # Relationships
    user = relationship("User", back_populates="bookmarks")
    book = relationship("Book", back_populates="bookmarks")