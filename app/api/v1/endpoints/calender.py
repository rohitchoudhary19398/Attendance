from typing import Any, List

from app import crud, schemas
from app.api.deps import get_current_user, get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/get", response_model=List[schemas.CalendarResponse])
def get_records(
    date: int = None,
    month: int = None,
    year: int = None,
    holiday: bool = None,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    objs = crud.calendar_obj.get_by_filters(
        db=db, date=date, month=month, year=year, is_holiday=holiday
    )
    return objs
