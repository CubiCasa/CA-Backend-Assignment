from flask_sqlalchemy import BaseQuery

from app.database import db
from sqlalchemy import inspect, DateTime


class BaseModel(db.Model):
    __abstract__ = True
    created_at = db.Column(DateTime, default=db.func.now())
    updated_at = db.Column(DateTime, default=db.func.now(), onupdate=db.func.now())
    deleted_at = db.Column(DateTime, nullable=True)

    def __init__(self):
        super(BaseModel, self).__init__()

    def serialize(self) -> dict:
        """Serialize the object attributes values into a dictionary."""

        return {}

    def remove_session(self):
        """Removes an object from the session its current session."""

        session = inspect(self).session
        if session:
            session.expunge(self)
