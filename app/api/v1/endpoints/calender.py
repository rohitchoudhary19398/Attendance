import os
from datetime import datetime
from typing import Any, List, Optional
from uuid import uuid4

from app import crud, schemas
from app.api.deps import get_current_user, get_db
from app.core.config import settings
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create", response_model=schemas.CalendarResponse)
def create_records(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    return None
