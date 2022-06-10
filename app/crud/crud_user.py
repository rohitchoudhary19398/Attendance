from app.crud.base import CRUDBase
from app.models.user import Users
from app.schemas import UserCreate, UserUpdate

from sqlalchemy.orm import Session
from ctlogging.config import get_logger


class CRUDUser(CRUDBase[Users, UserCreate, UserUpdate]):
    # Declare model specific CRUD operation methods.
    logger = get_logger(__name__)

    def get_by_username(self, db: Session, username: str) -> Users:
        return db.query(self.model).filter(Users.username == username).first()

    def get_by_email(self, db: Session, email: str) -> Users:
        return db.query(self.model).filter(Users.email == email).first()


users_obj = CRUDUser(Users)
