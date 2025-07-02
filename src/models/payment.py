from datetime import datetime
import uuid
from sqlalchemy import Column, String,Integer, DateTime, func, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class payment(Base):
    __tabelname__ = "payment"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    borrowing_id = Column(CHAR(36), ForeignKey("borrowing.id"), nullable=False)
    pick_up_id = Column(CHAR(36), ForeignKey("pickup.id"), nullable=True)
    payment_date = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    payment_method = Column(Enum("QRIS"), nullable=False)
    payment_price = Column(Integer)
    payment_totalprice = Column(Integer, nullable=False)
    pick_up_method = Column(Enum("COD", "Ambil Ditempat"), nullable=False)
    
    # Relationships
    borrowing = relationship("Borrowing", back_populates="payment")
    pick_up = relationship("PickUp", back_populates="payment")


    