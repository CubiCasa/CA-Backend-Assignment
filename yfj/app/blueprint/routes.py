import operator

import numpy as np
from app.database import delete_student_record
from app.database import filter_student_record_by_avg
from app.database import load_student_record
from app.database import update_job_record
from app.database import update_student_record
from app.utils import find_job
from flask import abort
from flask import Blueprint
from flask import jsonify
from flask import request as flask_request
from flask.wrappers import Response
from flask_pydantic import validate
from numpy.linalg import norm
from pydantic_models.grades import Grade
from pydantic_models.jobs import InputJob

bp = Blueprint('jobs', __name__, url_prefix='')


@bp.route('/<person_id>/advices', methods=['POST'])
@validate()
def advice_jobs(person_id: str) -> Response:
    advices = []
    default_advices = ['whatever you love!']

    grades = Grade.parse_obj(flask_request.get_json())
    avg_score = grades.avg_score()
    list_score = grades.get_list_score()

    update_student_record(person_id, grades)

    # filter down students with similar avg score
    data = filter_student_record_by_avg(avg_score)

    # no student with similar score -> send a general advices

    if data:
        jobs = {}
        for student in data:
            compare_list_score = student.get_list_score()
            cosine_similarity = np.dot(list_score, compare_list_score) / \
                (norm(list_score) * norm(compare_list_score))

            # filter down students with similar grades, add their jobs to recommendation.
            # if 1 job appear many times, multiple salary to use as indicator to match jobs
            if cosine_similarity > 0.9:
                for job in student.jobs:
                    if job.job_name not in jobs:
                        jobs[job.job_name] = job.salary
                    else:
                        jobs[job.job_name] += job.salary
        sorted_jobs = dict(
            sorted(jobs.items(), key=operator.itemgetter(1), reverse=True),
        )
        advices = list(sorted_jobs.keys())[:3]

    if not advices:
        advices = default_advices
    result = {
        'message': advices,
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
