from datetime import datetime
import uuid
from sqlalchemy import Column, String,Integer, DateTime, func, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    book_id = Column(CHAR(36), nullable=True)  # Optional, if the user has a book
    nik = Column(CHAR(36), nullable=False)
    fullname = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False, unique=True)
    gender = Column(Enum("Laki-laki", "Perempuan"), nullable=False)  # "Laki-laki" or "Perempuan"
    address = Column(String(255), nullable=True)
    date_of_birth = Column(DateTime(timezone=True), nullable=True)
    telephone = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    user_profile_url = Column(String(2048), nullable=True)
