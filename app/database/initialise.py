from sqlalchemy.orm import Session
from app.core.config import settings
from app.database.base_class import Base
from app.database.session import engine
from app import crud, schemas
from app.core.security import get_password_hash
from ctlogging.config import get_logger

logger = get_logger(__name__)


def initialise(db: Session) -> None:
    # Write database initialisation queries.
    Base.metadata.create_all(bind=engine)
    if settings.FIRST_SUPERUSER:
        user = crud.users_obj.get_by_email(db, email=settings.FIRST_SUPERUSER_EMAIL)
        if not user:
            user_in = schemas.UserCreate(
                username=settings.FIRST_SUPERUSER,
                full_name="Initial Super User",
                hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PW),
                email=settings.FIRST_SUPERUSER_EMAIL,
                is_superuser=1,
            )
            user = crud.users_obj.create(db, obj_in=user_in)  # noqa: F841
        else:
            logger.warning(
                "Skipping creating superuser. User with email "
                f"{settings.FIRST_SUPERUSER} already exists. "
            )
    else:
        logger.warning(
            "Skipping creating superuser.  FIRST_SUPERUSER needs to be "
            "provided as an env variable. "
            "e.g.  FIRST_SUPERUSER=admin"
        )
