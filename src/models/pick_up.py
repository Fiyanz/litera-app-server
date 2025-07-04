import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class PickUp(Base):
    __tablename__ = "pickup"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    borrowing_date = Column(DateTime(timezone=True), nullable=False)
    image_pickup_url = Column(String(2048), nullable=True)
    

    