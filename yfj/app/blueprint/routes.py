from app.database import create_student_record
from app.database import delete_student_record
from app.database import load_student_record
from app.database import update_job_record
from app.utils import find_job
from flask import abort
from flask import Blueprint
from flask import jsonify
from flask import request as flask_request
from flask.wrappers import Response
from flask_pydantic import validate
from pydantic_models.grades import Grade
from pydantic_models.jobs import Advices
from pydantic_models.jobs import InputJob

bp = Blueprint('jobs', __name__, url_prefix='')


@bp.route('/<person_id>/advices', methods=['POST'])
@validate()
def advice_job(person_id: str) -> Response:
    grades = Grade.parse_obj(flask_request.get_json())
    create_student_record(person_id, grades)
    # some computation
    advices = Advices(
        advices=[{'name': 'doctor'}, {'name': 'engineer'}, {'name': 'singer'}],
    )
    result = {
        'message': advices.dict(),
        'status': 'success',
    }
    return jsonify(result)


@bp.route('/<person_id>/delete_grades', methods=['POST'])
@validate()
def delete_grade(person_id: str) -> Response:
    delete_student_record(person_id)
    result_msg = {
        'message': 'deleted grades',
        'status': 'success',
    }
    return jsonify(result_msg)


@bp.route('/<person_id>/jobs', methods=['POST'])
@validate()
def add_jobs(person_id: str) -> Response:
    input_jobs = InputJob.parse_obj(flask_request.get_json())
    data = load_student_record(person_id)
    if data is None:
        abort(404, description="This student haven't had grades yet.")
    else:
        for job in input_jobs.jobs:
            result = find_job(job.name)
            update_job_record(person_id, result)
    result_msg = {
        'message': input_jobs.dict(),
        'status': 'success',
    }
    return jsonify(result_msg)
