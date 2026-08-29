from fastapi import APIRouter

from app.schemas.user import UserCreate
from app.database.mongodb import users_collection,otp_collection
from app.services.auth_service import hash_password
from app.models.user import User
from app.models.otp import OTPVerification
from app.services.otp_service import generate_otp,hash_otp,get_otp_expiry
from app.services.email_service import send_email

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

    result= users_collection.insert_one(new_user.model_dump())
    otp=generate_otp()
    otp_hash=hash_otp(otp)
    expires_at=get_otp_expiry()

    otp_record =OTPVerification(
        user_id=str(result.inserted_id),
        otp_hash=otp_hash,
        purpose="signup",
        expires_at=expires_at
        )
    otp_collection.insert_one(otp_record.model_dump())
    return{
        "message":"User Created Successfully!"
    }

@router.get("/test-email")
async def test_email():
    await send_email(
        to_email="deyoti2034@kikaga.com",
        subject="resume editor test",
        html="<h1>resend is working</h1><p>this is a text gmail</p>"
        )
    return {"message":"test email sent"}