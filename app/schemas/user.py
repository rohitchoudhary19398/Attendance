from typing import Optional
from pydantic import BaseModel
from uuid import uuid4


class User(BaseModel):
    id: Optional[str]
    username: Optional[str]
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[int] = 0
    is_superuser: Optional[int] = 0


class UserInDB(User):
    hashed_password: str


class UserCreate(User):
    id: str = str(uuid4().hex)
    username: str
    hashed_password: str
    email: str


class UserSignUp(BaseModel):
    username: str
    email: str
    password: str
    full_name: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserUpdate(User):
    id: str


class UserResponse(User):
    class Config:
        orm_mode = True
