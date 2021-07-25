from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from .database import Base
from .mixins import DictMixIn

class Record(Base, DictMixIn):
    __tablename__ = 'Records'

    # whether the datatypes are instantiated or passed as class, it is the same
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(Date)
    country = Column(String, index=True)
    cases = Column(Integer)

