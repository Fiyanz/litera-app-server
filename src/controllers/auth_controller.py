from datetime import datetime
from fastapi import APIRouter, File, Form, HTTPException, Depends, UploadFile
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user_schema import UserCreateSchema, UserLoginSchema
from ..db.database import get_db
from ..utils.response_wrapper import api_response
import bcrypt
from ..utils.cloudinary_uploader import upload_image

auth_route = APIRouter()

# auth signup
@auth_route.post("/signup/") 
async def signup(
    db: Session = Depends(get_db),
    nik: str = Form(...),
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    birth_date: str = Form(...),
    address: str = Form(...),
    gender: str = Form(...),
    ktp_image_url: UploadFile = File(...),
    ):
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email Already Registered")
    
    try:
        image_url = upload_image(ktp_image_url , 'ktp_image')
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    
    try:
        birth_date_obj = datetime.strptime(birth_date, '%Y-%m-%d').date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Format tanggal lahir salah. Gunakan YYYY-MM-DD.")

    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    user_data = {
        "nik": nik,
        "name": name,
        "email": email,
        "password": password_hash.decode('utf-8'),
        "birth_date": birth_date_obj,
        "address": address,
        "gender": gender,
        "ktp_image_url": image_url['url'],
        "ktp_image_public_id": image_url['public_id']
    }
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return api_response(
        data=new_user,
        message="User successfully registered"
    )

# auth login
@auth_route.post("/signin/")
async def login(user: UserLoginSchema, db: Session = Depends(get_db)): 
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Email tidak ditemukan")

    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Password salah")
    
    # decode the password
    # if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password):
    #     raise HTTPException(status_code=400, detail="Invalid password")
    
    return api_response(
        data=db_user,
        message="Login successful"
    )