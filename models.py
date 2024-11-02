from sqlalchemy import Column, Date, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    full_name = Column(String(255), nullable=False, index=True)
    birth_date = Column(Date, nullable=False)
    sex = Column(String(10), nullable=False, index=True)
