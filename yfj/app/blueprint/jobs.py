import os
from typing import Optional

from app.database import db
from app.models import Student
from cryptography.fernet import Fernet
from flask import abort
from flask import Blueprint
from flask import jsonify
from flask.wrappers import Response
from flask_pydantic import validate
from models.advices import Advices
from models.advices import InputJob
from models.grades import Grade

bp = Blueprint('jobs', __name__, url_prefix='')
key = os.environ.get('ENCRYPT_KEY')
fernet = Fernet(key)


@bp.route('/<person_id>/advices', methods=['POST'])
@validate()
def advice_job(person_id: str, body: Grade) -> Response:
    # some computation

    student = Student(
        student_id=person_id,
        math=body.math,
        physics=body.physics,
        chemistry=body.chemistry,
        biology=body.biology,
        literature=body.literature,
        history=body.history,
        philosophy=body.philosophy,
        art=body.art,
        foreign_lang=body.foreign_lang,
    )
    db.session.add(student)
    db.session.commit()

    # some computation
    advices = Advices(
        advices=[{'name': 'doctor'}, {'name': 'engineer'}, {'name': 'singer'}],
    )
    result = {
        'message': advices.dict(),
        'status': 'success',
    }
    return jsonify(result)


@bp.route('/<person_id>/jobs', methods=['POST'])
@validate()
def add_jobs(person_id: str, body: InputJob) -> Response:
    data = load_student_record(person_id)
    if data is None:
        abort(404, description="This student haven't had grades yet.")
    # else:
        # find job in job_earning
        # update to job db

    result_msg = {
        'message': body.dict(),
        'status': 'success',
    }
    return jsonify(result_msg)


def load_student_record(person_id: str) -> Optional[Student]:
    encrypted_id = fernet.encrypt(person_id.encode()).decode('ascii')
    data = db.session.query(Student).filter(
        Student.student_id == encrypted_id,
    )
    return data.first()
