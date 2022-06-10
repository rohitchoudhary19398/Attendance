from datetime import timedelta
from typing import Any

from app import crud, schemas
from app.api import deps
from app.core.auth import authenticate_user, create_access_token
from app.core.config import settings
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from app.core.security import get_password_hash

router = APIRouter()


@router.post("/signup", response_model=schemas.user.UserResponse, status_code=201)
def create_user_signup(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.user.UserSignUp,
) -> Any:
    """
    Create new user without the need to be logged in.
    """

    user = crud.users_obj.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )

    user = crud.users_obj.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )

    hashed_password = get_password_hash(user_in.password)
    new_user = schemas.user.UserCreate(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_password,
        full_name=user_in.full_name,
    )
    user = crud.users_obj.create(db=db, obj_in=new_user)
    return user


@router.post("/login", response_model=schemas.Token)
async def login(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = authenticate_user(
        db=db, username=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.SECURITY.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/current_user", response_model=schemas.User)
async def read_users_me(
    current_user: schemas.User = Depends(deps.get_current_active_user),
):
    return current_user
