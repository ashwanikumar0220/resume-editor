from fastapi import FastAPI
from app.database import mongodb
from app.routes.auth import router as auth_router

app=FastAPI()

app.include_router(auth_router)

@app.get("/")
def home():
    return{"message":"App is running!"}

