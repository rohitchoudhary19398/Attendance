from sqlalchemy import Column, String, DateTime, Boolean, Float

from app.database.base_class import Base


class AttRecords(Base):
    __tablename__ = "att_records"

    id = Column(String(50), primary_key=True, index=True)
    user_id = Column(String(50))
    calender_id = Column(String(50))
    is_present = Column(Boolean)
    status = Column(String(30))
    in_time = Column(Float)
    out_time = Column(Float)
    created_date = Column(DateTime)
    updated_date = Column(DateTime)
