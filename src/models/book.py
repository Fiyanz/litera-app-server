import uuid
from sqlalchemy import Column, String,Integer, DateTime, func, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class Book(Base):
    __tablename__ = "book"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(CHAR(36), ForeignKey("user.user_id"))
    bookmark_id = Column(CHAR(36), ForeignKey("bookmark.id"), nullable=True)
    title = Column(String(255), nullable=False)
    writer = Column(String(255), nullable=False)
    publiser = Column(String(255))
    isbn = Column(CHAR(13), unique=True, nullable=False)
    published_date = Column(DateTime(timezone=True), nullable=True)
    price_per_day = Column(Integer, nullable=True)
    image_book_url = Column(String(2048), nullable=True)
    
    book_owner = relationship("User", back_populates="book")