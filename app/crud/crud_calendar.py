from app.crud.base import CRUDBase, ModelType
from app.models.calendar import Calendar
from app.schemas import CalendarCreate, CalendarUpdate

# from app.core.constants import FileStatus
from sqlalchemy.orm import Session
from typing import List
from ctlogging.config import get_logger
from sqlalchemy import TEXT


class CRUDCalendar(CRUDBase[Calendar, CalendarCreate, CalendarUpdate]):
    # Declare model specific CRUD operation methods.
    logger = get_logger(__name__)

    def get_by_filters(
        self, db: Session, *, skip: int = 0, limit: int = 100, status: TEXT = None
    ) -> List[ModelType]:
        query = db.query(self.model)
        if status:
            query = query.filter(Calendar.status == status)
        return query.all()


calendar_obj = CRUDCalendar(Calendar)
