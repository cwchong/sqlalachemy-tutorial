"""
Simple reader to verify database loaded
"""
from app import models
from app.database import SessionLocal
from sqlalchemy import select

db = SessionLocal()

print('records', '='*20)
query = select([models.Record]).limit(5)
res = db.execute(query)
for record_obj in res.scalars():
    print(f"{record_obj.id}::{record_obj.country}::{record_obj.cases}::{record_obj.date}")

print('users', '='*20)
query = select([models.User]).limit(5)
res = db.execute(query)
for record_obj in res.scalars():
    print(f"{record_obj.id}::{record_obj.name}::{record_obj.age}")

db.close()