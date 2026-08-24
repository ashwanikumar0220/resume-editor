from datetime import UTC, datetime
from pydantic import BaseModel,Field

class User(BaseModel):
    name:str
    email:str
    password_hash:str
    is_verified:bool=False
    role:str="user"
    created_at:int=Field(default_factory=lambda:int(datetime.now(UTC).timestamp()))
