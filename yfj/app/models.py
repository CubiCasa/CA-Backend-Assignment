from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.database import db


class Test(db.Model):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
