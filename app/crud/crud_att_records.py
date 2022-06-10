from app.crud.base import CRUDBase
from app.models.att_records import AttRecords
from app.schemas import AttRecordsCreate, AttRecordsUpdate

# from app.core.constants import FileStatus
from sqlalchemy.orm import Session
from typing import List
from ctlogging.config import get_logger


class CRUDAttRecords(CRUDBase[AttRecords, AttRecordsCreate, AttRecordsUpdate]):
    # Declare model specific CRUD operation methods.
    logger = get_logger(__name__)

    def get_by_user_id(self, db: Session, user_id: str = None) -> List[AttRecords]:
        self.logger.info("get_by_user_id")
        print("get_by_user_id")
        query = db.query(self.model)
        print(query)
        if user_id is not None:
            query = query.filter(AttRecords.user_id == user_id)
        print(query)
        return query.all()


attrecords_obj = CRUDAttRecords(AttRecords)
