from app import crud
from app.api.deps import get_db
from app.core.security import verify_password
from fastapi import Depends
from sqlalchemy.orm.session import Session
from datetime import datetime, timedelta
from typing import Optional

from app.core.config import settings
from jose import jwt


def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = crud.users_obj.get_by_username(db=db, username=username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECURITY.SECRET_KEY, algorithm=settings.SECURITY.ALGORITHM
    )
    return encoded_jwt
