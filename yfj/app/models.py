import os

from app.database import db
from cryptography.fernet import Fernet
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata
key = os.environ.get('ENCRYPT_KEY')
fernet = Fernet(key)


class StudentJob(Base):
    __tablename__ = 'student_job'
    student_id = db.Column(
        db.Integer, db.ForeignKey(
            'student.id',
        ), primary_key=True,
    )
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), primary_key=True)


class Student(Base):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    student_id = db.Column(db.String)
    math = db.Column(db.Integer, nullable=False)
    physics = db.Column(db.Integer, nullable=False)
    chemistry = db.Column(db.Integer, nullable=False)
    biology = db.Column(db.Integer, nullable=False)
    literature = db.Column(db.Integer, nullable=False)
    history = db.Column(db.Integer, nullable=False)
    philosophy = db.Column(db.Integer, nullable=False)
    art = db.Column(db.Integer, nullable=False)
    foreign_lang = db.Column(db.Integer, nullable=False)
    jobs = relationship('Job', secondary='student_job')

    def __init__(
        self, student_id, math, physics, chemistry, biology, literature,
        history, philosophy, art, foreign_lang,
    ):
        self.student_id = fernet.encrypt(student_id.encode()).decode('ascii')
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology
        self.literature = literature
        self.history = history
        self.philosophy = philosophy
        self.art = art
        self.foreign_lang = foreign_lang


class Job(Base):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True, autoincrement='auto')
    job_name = db.Column(db.String)
    salary = db.Column(db.Integer, nullable=False)
    students = relationship('Student', secondary='student_job')
