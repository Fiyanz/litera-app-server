from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR
from ..db.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nik = Column(CHAR(36), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    birth_date = Column(DateTime(timezone=True), nullable=True)
    gender = Column(String(10), nullable=True)
    address = Column(String(255), nullable=True)
    ktp_image_url = Column(String(2048), nullable=True)
    ktp_image_public_id = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    profile = relationship("UserProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(CHAR(36), ForeignKey('users.id'), nullable=False)
    profile_image_url  = Column(String(2048), nullable=True)
    profile_image_public_id = Column(String(255), nullable=True)

    user = relationship("User", back_populates="profile")
