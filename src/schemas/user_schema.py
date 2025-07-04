from pydantic import BaseModel, EmailStr, ConfigDict, HttpUrl
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    nik: Optional[str] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    birth_date: Optional[datetime] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    created_at: Optional[datetime] = None
    ktp_image_url : Optional[HttpUrl] = None
    ktp_image_public_id : Optional[str] = None

    profile : Optional['UserProfileSchema'] = None

    # set orm
    model_config = ConfigDict(from_attributes=True)

class UserCreateSchema(BaseModel):
    nik: Optional[str] = None
    name: Optional[str] = None
    email: EmailStr
    password: Optional[str] = None
    birth_date: Optional[datetime] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    ktp_image_url : Optional[HttpUrl] = None
    ktp_image_public_id: Optional[str] = None

    # set orm
    model_config = ConfigDict(from_attributes=True)

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

    # set orm
    model_config = ConfigDict(from_attributes=True)

class UserUpdateSchema(BaseModel):
    nik: Optional[str] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    profile_image_url : Optional[HttpUrl] = None
    profile_image_public_id: Optional[str] = None

    # set orm
    model_config = ConfigDict(from_attributes=True)

class UserProfileSchema(BaseModel):
    user_id: str
    profile_image_url: Optional[HttpUrl] = None
    profile_image_public_id: Optional[str] = None

    # set orm
    model_config = ConfigDict(from_attributes=True)