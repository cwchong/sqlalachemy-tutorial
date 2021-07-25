"""
Creates the database and loads it with data,
without going through the app, but still sharing the same
db engine and table schema definitions
"""
import csv
import datetime

from app import models
from app.database import SessionLocal, engine

db = SessionLocal()

# create tables if not exist; does not update existing tables if schema changed
models.Base.metadata.create_all(bind=engine)

with open('sars_2003_complete_dataset_clean.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    
    for row in csv_reader:
        db_record = models.Record(
            date=datetime.datetime.strptime(row['date'], '%Y-%m-%d'),
            country=row['country'],
            cases=row['cases'],
        )
        db.add(db_record)
    db.commit() # so we can add in bulk; autocommit is false
db.close()