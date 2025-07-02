import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class PickUp(Base):
    __tablename__ = "pick_up"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    borrowing_id = Column(CHAR(36), ForeignKey("borrowing.id"), nullable=False)
    book_id = Column(CHAR(36), ForeignKey("book.id"), nullable=False)
    image_pick_up_url = Column(String(2048), nullable=True)


    borrowing = relationship("Borrowing", back_populates="pick_ups")
    book = relationship("Book", back_populates="pick_ups")
