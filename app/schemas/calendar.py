from typing import Optional

from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4


class CalendarBase(BaseModel):
    id: Optional[str]
    date: Optional[int]
    month: Optional[int]
    year: Optional[int]
    day: Optional[int]
    is_holiday: Optional[bool]
    hoilday_description: Optional[str]
    created_date: Optional[datetime]
    updated_date: Optional[datetime]


class CalendarCreate(CalendarBase):
    id: str


class CalendarUpdate(CalendarBase):
    id: str


class CalendarResponse(CalendarBase):
    class Config:
        orm_mode = True
