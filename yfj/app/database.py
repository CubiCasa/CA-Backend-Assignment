"""This module provides means to perform operations on the database
using the SQLAlchemy library."""
import os
from typing import Optional

import numpy as np
from cryptography.fernet import Fernet
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from pydantic_models.grades import Grade as PydanticGrade
from pydantic_models.jobs import JobPydantic
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

db = SQLAlchemy()
migrate = Migrate()

Base = declarative_base()
metadata = Base.metadata
key = os.environ.get(
    'ENCRYPT_KEY', '=nYRiebe_90xmDXHA16424JOgb9om9sbp9OV7Z-1ONl1=',
)
fernet = Fernet(key)


def init(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)


class StudentJob(Base):
    __tablename__ = 'student_job'
    student_id = Column(
        Integer, ForeignKey(
            'student.id',
        ), primary_key=True,
    )
    job_id = Column(Integer, ForeignKey('job.id'), primary_key=True)


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    student_id = Column(String)
    math = Column(Integer, nullable=False)
    physics = Column(Integer, nullable=False)
    chemistry = Column(Integer, nullable=False)
    biology = Column(Integer, nullable=False)
    literature = Column(Integer, nullable=False)
    history = Column(Integer, nullable=False)
    philosophy = Column(Integer, nullable=False)
    art = Column(Integer, nullable=False)
    foreign_lang = Column(Integer, nullable=False)
    average_score = Column(Float)
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
        self.average_score = (
            math + physics + chemistry + biology +
            literature + history + philosophy + art + foreign_lang
        ) / 9

    def get_list_score(self) -> np.array:
        return np.array([
            self.math, self.physics, self.chemistry, self.biology,
            self.literature, self.history, self.philosophy, self.art, self.foreign_lang,
        ])


class Job(Base):
    __tablename__ = 'job'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    job_name = Column(String)
    salary = Column(Integer, nullable=False)
    students = relationship('Student', secondary='student_job')


def create_student_record(person_id: str, grades: PydanticGrade) -> None:
    student = Student(
        student_id=person_id,
        math=grades.math,
        physics=grades.physics,
        chemistry=grades.chemistry,
        biology=grades.biology,
        literature=grades.literature,
        history=grades.history,
        philosophy=grades.philosophy,
        art=grades.art,
        foreign_lang=grades.foreign_lang,
    )
    db.session.add(student)
    return db.session.commit()


def load_student_record(person_id: str) -> Optional[Student]:

    encrypted_id = fernet.encrypt(person_id.encode()).decode('ascii')
    data = db.session.query(Student).filter(
        Student.student_id == encrypted_id,
    )
    return data.first()


def filter_student_record_by_avg(avg_score: float) -> Optional[list[Student]]:

    data = db.session.query(Student).filter(
        abs(avg_score - Student.average_score) <= 1,
    )
    return data.all()


def delete_student_record(person_id: str) -> None:
    encrypted_id = fernet.encrypt(person_id.encode()).decode('ascii')
    data = db.session.query(Student).filter(
        Student.student_id == encrypted_id,
    )
    return data.delete()


def create_job_record(job_object: JobPydantic, student_record: Student) -> None:
    job = Job(
        job_name=job_object.name,
        salary=job_object.salary,
    )
    job.students.append(student_record)
    db.session.add(job)
    return db.session.commit()


def load_job_record(job_name: str) -> Optional[Job]:
    data = db.session.query(Job).filter(
        Job.job_name == job_name,
    )
    return data.first()


def update_job_record(person_id: str, job: JobPydantic) -> None:
    student_record = load_student_record(person_id)

    job_record = load_job_record(job.name)
    if not job_record:
        create_job_record(job, student_record)
    else:
        job_record.salary = job.salary
        job_record.students.append(student_record)
        db.session.add(job_record)
        db.session.commit()
    return None
