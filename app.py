from fastapi import FastAPI
from src.controllers.user_controller import route as user_router
from src.db.database import create_tabels

app = FastAPI()

app.include_router(user_router, prefix="/api", tags=["Users"])
app.include_router(create_tabels, prefix="/api", tags=["Auth"])

create_tabels()

@app.get("/")
def root():
    return {"message": "Welcome to the FasyAPI CRUD API"}