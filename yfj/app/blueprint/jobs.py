from flask import Blueprint
from flask import jsonify
from flask.wrappers import Response
from flask_pydantic import validate

from app.database import db
from app.models import Student
from models.advices import Advices
from models.advices import InputJob
from models.grades import Grade

bp = Blueprint('jobs', __name__, url_prefix='')


@bp.route('/<person_id>/advices', methods=['POST'])
@validate()
def advice_job(person_id: str, body: Grade) -> str:
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
        foreign_lang=body.foreign_lang
    )
    db.session.add(student)
    db.session.commit()

    # some computation
    result = Advices(
        advices=[{'name': 'doctor'}, {'name': 'engineer'}, {'name': 'singer'}],
    )
    return result.json()


@bp.route('/<person_id>/jobs', methods=['POST'])
@validate()
def add_jobs(person_id: int, body: InputJob) -> Response:
    # some computation
    result_msg = {'message': body.dict()}
    return jsonify(result_msg)
