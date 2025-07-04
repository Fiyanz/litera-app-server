import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class Return(Base):
    __tablename__ = "return"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    riturn_date = Column(DateTime(timezone=True), nullable=False)
    image_return_url = Column(String(2048), nullable=True)
    