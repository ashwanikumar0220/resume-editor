from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.database.mongodb import users_collection
from app.services.auth_service import hash_password
from app.models.user import User

router = APIRouter()

@router.post("/signup")
def signup(user:UserCreate):
    existing_user=users_collection.find_one({"email":user.email})

    if existing_user:
        return{"message":"email already exists!"}

    hashed_password=hash_password(user.password)
    new_user=User(
        name=user.name,
        email=user.email,
        password_hash=hashed_password
    )

    users_collection.insert_one(new_user.model_dump())

    return{
        "message":"User Created Successfully!"
    }