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


class UserRetrievedUpdate(BaseResource):
    parser = reqparse.RequestParser()
    user_repository = UserRepository()

    def get(self, id):
        """
            This api help get a user
        """
        user_repository = UserRepository()
        user = user_repository.get(id)
        if not user:
            abort(404, message=TranslationText.UserNotFound)
        return user.to_dict()

    def put(self, id):
        """
            This api help update a user
        """
        user = self.user_repository.get(id)
        if not user:
            abort(404)
        self.parser.add_argument('username', type=str, required=True, help='Username is required')
        self.parser.add_argument('first_name', type=str, required=True, help='First name is required')
        self.parser.add_argument('last_name', type=str, required=True, help='Last name is required')
        self.parser.add_argument('email', type=str, required=True, help='Email is required')
        self.parser.add_argument('address', type=str, required=False)
        self.parser.add_argument('school_name', type=str, required=False)
        self.parser.add_argument('user_type', type=int, required=True)
        self.parser.add_argument('gender', type=int, required=True)
        args = self.parser.parse_args()

        user.username = args.get('username')
        user.first_name = args.get('first_name')
        user.last_name = args.get('last_name')
        user.email = args.get('email')
        user.address = args.get('address')
        user.school_name = args.get('school_name')
        user.user_type = UserTypes(args.get('user_type'))
        user.gender = Genders(args.get('gender'))
        self.user_repository.update(user)

        return user.to_dict(rules=('-password',))

    def delete(self, id):
        """
            This api help delete a user
        """
        user = self.user_repository.get(id)
        if not user:
            abort(404)
        self.user_repository.delete(user)
        return None


class UserListAddSchoolPerformance(BaseResource):
    parser = reqparse.RequestParser()
    user_performance_repository = UserSchoolPerformanceRepository()

    def get(self, id):
        """
            This api help add a performance
        """
        args = request.args
        query = UserSchoolPerformance.query.filter(UserSchoolPerformance.user_id == id)
        return self.get_paginated_list(UserSchoolPerformance, page=args.get('page', Pagination.DefaultPage),
                                       limit=args.get('limit', Pagination.DefaultLimit), init_query=query)

    def post(self, id):
        """
            This api help add a performance
        """
        self.parser.add_argument('math', type=float, required=True, help=TranslationText.MathIsRequired)
        self.parser.add_argument('physics', type=float, required=True, help=TranslationText.MathIsRequired)
        self.parser.add_argument('chemistry', type=float, required=True, help=TranslationText.ChemistryIsRequired)
        self.parser.add_argument('biology', type=float, required=True, help=TranslationText.BiologyIsRequired)
        self.parser.add_argument('literature', type=float, required=True, help=TranslationText.LiteratureIsRequired)
        self.parser.add_argument('history', type=float, required=True, help=TranslationText.HistoryIsRequired)
        self.parser.add_argument('geography', type=float, required=True, help=TranslationText.GeographyIsRequired)
        self.parser.add_argument('phylosophy', type=float, required=True, help=TranslationText.PhylosophyIsRequired)
        self.parser.add_argument('art', type=float, required=True, help=TranslationText.ArtIsRequired)
        self.parser.add_argument('foreign_language', type=int, required=True, help=TranslationText.ForeignIsRequired)
        args = self.parser.parse_args()
        args['user_id'] = id
        user_performance = UserSchoolPerformance(**args)
        self.user_performance_repository.save(user_performance)

        return user_performance.to_dict()


class UserRetrieveUpdateSchoolPerformance(BaseResource):
    parser = reqparse.RequestParser()
    user_performance_repository = UserSchoolPerformanceRepository()
    user_repository = UserRepository()

    def get(self, id):
        """
            This api help add a performance
        """
        performance = UserSchoolPerformance.query.filter(UserSchoolPerformance.id == id).first()
        if not performance:
            abort(404, message=TranslationText.PerformanceNotFound)
        return performance.to_dict()

    def put(self, id):
        """
            This api help update a performance
        """
        user_performance = self.user_performance_repository.get(id)
        if not user_performance:
            abort(404, message=TranslationText.PerformanceNotFound)
        self.parser.add_argument('math', type=float, required=True, help=TranslationText.MathIsRequired)
        self.parser.add_argument('physics', type=float, required=True, help=TranslationText.MathIsRequired)
        self.parser.add_argument('chemistry', type=float, required=True, help=TranslationText.ChemistryIsRequired)
        self.parser.add_argument('biology', type=float, required=True, help=TranslationText.BiologyIsRequired)
        self.parser.add_argument('literature', type=float, required=True, help=TranslationText.LiteratureIsRequired)
        self.parser.add_argument('history', type=float, required=True, help=TranslationText.HistoryIsRequired)
        self.parser.add_argument('geography', type=float, required=True, help=TranslationText.GeographyIsRequired)
        self.parser.add_argument('phylosophy', type=float, required=True, help=TranslationText.PhylosophyIsRequired)
        self.parser.add_argument('art', type=float, required=True, help=TranslationText.ArtIsRequired)
        self.parser.add_argument('foreign_language', type=int, required=True, help=TranslationText.ForeignIsRequired)

        args = self.parser.parse_args()
        user_performance.math = args.get('math')
        user_performance.physics = args.get('physics')
        user_performance.chemistry = args.get('chemistry')
        user_performance.biology = args.get('biology')
        user_performance.literature = args.get('literature')
        user_performance.history = args.get('history')
        user_performance.geography = args.get('geography')
        user_performance.phylosophy = args.get('phylosophy')
        user_performance.art = args.get('art')

        self.user_performance_repository.update(user_performance)

        return user_performance.to_dict()

    def delete(self, id):
        """
            This api help delete a performance
        """
        performance = self.user_performance_repository.get(id)
        if not performance:
            abort(404, message=TranslationText.PerformanceNotFound)
        self.user_performance_repository.delete(performance)
        return None


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
