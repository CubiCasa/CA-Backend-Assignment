"""Blueprint to organize and group, views related
to the '/users' endpoint of HTTP REST API.
"""

from flask import (Blueprint)
from flask import request
import pandas as pd
import numpy as np
from sklearn import linear_model

from app.base.api_client import ApiClient
from app.base.base_resource import BaseResource
from app.base.constants import UserTypes, Genders, TranslationText, Pagination
from app.base.custom_api import CustomApi
from app.model import UserRepository, User
from flask_restful import reqparse, abort

from app.model.models import UserSchoolPerformance
from app.model.user_school_performance_repository import UserSchoolPerformanceRepository

bp = Blueprint('users', __name__, url_prefix='/users')
api = CustomApi(bp)


class UserListAdd(BaseResource):

    def get(self):
        """
                This api get all users
        """
        args = request.args
        return self.get_paginated_list(User, page=args.get('page', Pagination.DefaultPage),
                                       limit=args.get('limit', Pagination.DefaultLimit))

    def post(self):
        """
                This api help add a user
        """
        self.parser.add_argument('username', type=str, required=True, help='Username is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')
        self.parser.add_argument('first_name', type=str, required=True, help='First name is required')
        self.parser.add_argument('last_name', type=str, required=True, help='Last name is required')
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('address', type=str, required=False)
        self.parser.add_argument('school_name', type=str, required=False)
        self.parser.add_argument('user_type', type=int, required=True)
        self.parser.add_argument('gender', type=int, required=True)
        args = self.parser.parse_args()
        user = User(username=args.get('username'), first_name=args.get('first_name'), last_name=args.get('last_name'),
                    email=args.get('email'), address=args.get('address'), school_name=args.get('school_name'),
                    user_type=UserTypes(args.get('user_type')), gender=Genders(args.get('gender')),
                    password=args.get('password'))
        user_repository = UserRepository()
        user_repository.save(user)

        return user.to_dict(rules=('-password',))


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
