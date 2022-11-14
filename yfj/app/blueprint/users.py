"""Blueprint to organize and group, views related
to the '/users' endpoint of HTTP REST API.
"""

from flask import (
    abort, Blueprint, request, Response, make_response, jsonify
)
from app.model import UserRepository
from flask_restful import Api, Resource

bp = Blueprint('users', __name__, url_prefix='/users')
api = Api(bp)


class UserListAdd(Resource):
    def get(self):
        return {'task': 'get user list'}

    def post(self):
        return {'task': 'add a user'}


class UserRetrievedUpdate(Resource):
    def get(self, id):
        return {'task': 'Get a user'}

    def put(self, id):
        return {'task': 'Update a user'}

    def delete(self, id):
        return {'task': 'Delete a user'}


class UserListAddSchoolPerformance(Resource):
    def get(self, id):
        return {'task': 'Get list school performance for a user'}

    def post(self, id):
        return {'task': 'Add a school performance for a user'}


class UserRetrieveUpdateSchoolPerformance(Resource):
    def get(self, id):
        return {'task': 'Get a school performance for a user'}

    def put(self, id):
        return {'task': 'Update a school performance for a user'}

    def delete(self, id):
        return {'task': 'Delete a school performance'}


class UserGetAdviceJobs(Resource):
    def get(self, id):
        return {'task': 'get advice jobs'}


class UserPostCurrentJobs(Resource):
    def post(self, id):
        return {'task': 'Update current jobs'}


api.add_resource(UserListAdd, '')
api.add_resource(UserRetrievedUpdate, '/<int:id>')
api.add_resource(UserListAddSchoolPerformance, '/<int:id>/school_performances')
api.add_resource(UserRetrieveUpdateSchoolPerformance, '/users/school_performances/<int:id>')
api.add_resource(UserGetAdviceJobs, '/<int:id>/advices')
api.add_resource(UserPostCurrentJobs, '/<int:id>/jobs')
