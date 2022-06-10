from typing import Optional

from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4


class AttRecordsBase(BaseModel):
    id: Optional[str]
    user_id: Optional[str]
    calender_id: Optional[str]
    is_present: Optional[bool]
    status: Optional[str]
    in_time: Optional[float]
    out_time: Optional[float]
    created_date: Optional[datetime]
    updated_date: Optional[datetime]


class AttRecordsCreate(AttRecordsBase):
    id: str = str(uuid4().hex)


class AttRecordsUpdate(AttRecordsBase):
    id: str


class AttRecordsResponse(AttRecordsBase):
    class Config:
        orm_mode = True
