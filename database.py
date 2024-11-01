from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import DATABASE_URI


engine = create_engine(DATABASE_URI)
session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


