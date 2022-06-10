from sqlalchemy import Column, VARCHAR, INTEGER


from app.database.base_class import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(VARCHAR(50), primary_key=True, index=True)
    username = Column(VARCHAR(50), nullable=False)
    full_name = Column(VARCHAR(100), nullable=True)
    email = Column(VARCHAR(30), nullable=False)
    hashed_password = Column(VARCHAR(200), nullable=False)
    disabled = Column(INTEGER)
    is_superuser = Column(INTEGER, default=0)
