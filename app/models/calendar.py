from sqlalchemy import Column, String, DateTime, Integer, Boolean

from app.database.base_class import Base


class Calendar(Base):
    __tablename__ = "calendar"

    id = Column(String(50), primary_key=True, index=True)
    date = Column(Integer)
    month = Column(Integer)
    year = Column(Integer)
    day = Column(String(30))
    is_holiday = Column(Boolean)
    hoilday_description = Column(String(200))
    created_date = Column(DateTime)
    updated_date = Column(DateTime)
