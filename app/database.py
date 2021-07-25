from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

DB_URL = 'sqlite:///./test.db'

engine = create_engine(DB_URL, connect_args={'check_same_thread': False})
# factory; this creates a scoped session that helps resolve threading issue
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

