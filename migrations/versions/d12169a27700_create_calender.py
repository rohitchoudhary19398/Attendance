"""create calender

Revision ID: d12169a27700
Revises: 
Create Date: 2022-06-07 10:23:06.197531

"""
from alembic import op
import sqlalchemy as sa
from app import crud, schemas
from app.database import session
from alembic import context
import logging

logger = logging.getLogger("alembic")

# revision identifiers, used by Alembic.
revision = "d12169a27700"
down_revision = None
branch_labels = None
depends_on = None


config = context.config


def upgrade():
    db = session.SessionLocal()
    import datetime
    from pandas import date_range

    cd = datetime.datetime.now()
    year = cd.year
    obj_ins = [
        schemas.CalendarCreate(
            id=d.strftime("%d/%m/%Y"),
            date=d.day,
            month=d.month,
            year=d.year,
            day=d.weekday(),
            created_date=cd,
        )
        for d in date_range(f"01/01/{year}", f"31/12/{year}")
    ]
    try:
        crud.calendar_obj.create_bulk(db=db, obj_ins=obj_ins)
    except Exception as e:
        logger.error("Failed to create calender")
        logger.exception(e)


def downgrade():
    pass
