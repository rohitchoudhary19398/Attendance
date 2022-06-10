from datetime import datetime
from typing import Any, List

from app import crud, schemas
from app.api.deps import get_current_user, get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/add", response_model=schemas.AttRecordsResponse)
def create_records(
    date: str,
    in_time: str,
    out_time: str,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    try:
        att_rect = schemas.AttRecordsCreate(
            user_id=current_user.id,
            is_present=True,
            status="pending",
            in_time=in_time,
            out_time=out_time,
            calender_id=date,
            created_date=datetime.now()
        )
        response = crud.attrecords_obj.create(db=db, obj_in=att_rect)
        return response
    except Exception as e:
        print(e)


@router.post("/get", response_model=List[schemas.AttRecordsResponse])
def get_records(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    response = crud.attrecords_obj.get_by_user_id(db, current_user.id)
    return response
