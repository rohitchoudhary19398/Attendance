from app.crud.base import CRUDBase, ModelType
from app.models.att_records import AttRecords
from app.schemas import AttRecordsCreate, AttRecordsUpdate

# from app.core.constants import FileStatus
from sqlalchemy.orm import Session
from typing import List
from ctlogging.config import get_logger
from sqlalchemy import TEXT


class CRUDAttRecords(CRUDBase[AttRecords, AttRecordsCreate, AttRecordsUpdate]):
    # Declare model specific CRUD operation methods.
    logger = get_logger(__name__)

    def get_by_user_id(
        self, db: Session, *, skip: int = 0, limit: int = 100, user_id: TEXT = None
    ) -> List[AttRecords]:
        self.logger.info("get_by_user_id")
        print("get_by_user_id")
        query = db.query(self.model)
        print(query)
        if user_id:
            query = query.filter(AttRecords.user_id == user_id)
        print(query)
        return query.all()

    def get_by_filters(
        self, db: Session, *, skip: int = 0, limit: int = 100, status: TEXT = None
    ) -> List[AttRecords]:
        query = db.query(self.model)
        if status:
            query = query.filter(AttRecords.status == status)
        return query.all()


attrecords_obj = CRUDAttRecords(AttRecords)
