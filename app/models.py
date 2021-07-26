from sqlalchemy import Column, Integer, String, CheckConstraint, and_
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

class User(Base, DictMixIn):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)

    __table_args__ = (
        # ChcekConstraint can take 'sql statements for check'
        CheckConstraint(
            and_(
                age > 0,
                age < 100
            ), 
            name='valid_age'
        ),
        {} # just to force the wrapper to be a tuple, else has to declare with tuple()
    )