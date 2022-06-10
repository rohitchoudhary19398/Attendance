from app.crud.base import CRUDBase
from app.models.calendar import Calendar
from app.schemas import CalendarCreate, CalendarUpdate

from sqlalchemy.orm import Session
from typing import List
from ctlogging.config import get_logger


class CRUDCalendar(CRUDBase[Calendar, CalendarCreate, CalendarUpdate]):
    # Declare model specific CRUD operation methods.
    logger = get_logger(__name__)

    def get_all(self, db: Session) -> List[Calendar]:
        query = db.query(self.model)
        return query.all()

    def get_by_filters(
        self,
        db: Session,
        date: int = None,
        month: int = None,
        year: int = None,
        is_holiday: bool = None,
    ) -> List[Calendar]:
        query = db.query(self.model)
        if date is not None:
            query = query.filter(Calendar.date == date)
        if month is not None:
            query = query.filter(Calendar.month == month)
        if year is not None:
            query = query.filter(Calendar.year == year)
        if is_holiday is not None:
            query = query.filter(Calendar.is_holiday == is_holiday)
        return query.all()


calendar_obj = CRUDCalendar(Calendar)
