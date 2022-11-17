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


class UserGetAdviceJobs(BaseResource):
    parser = reqparse.RequestParser()
    user_performance_repository = UserSchoolPerformanceRepository()
    user_repository = UserRepository()

    def get_list_job(self):
        api_client = ApiClient()
        return api_client.get('/job_earnings')

    def calculate_r2(self, row, performance_x):
        performance_y = np.array(
            list([row['math'], row['physics'], row['chemistry'], row['biology'], row['literature'], row['history'],
                  row['geography'], row['phylosophy'], row['art'], row['foreign_language']])).reshape(-1, 1)
        model_data = linear_model.LinearRegression()
        mwr = model_data.fit(performance_x, performance_y)
        return mwr.score(performance_x, performance_y)

    def get_3_jobs(self, user_ids):
        jobs = []
        for user_id in user_ids:
            match_user = self.user_repository.get(user_id)
            if match_user:
                for job in match_user.jobs:
                    jobs.append(job)
                    if len(jobs) >= 3:
                        return jobs
        return jobs

    def get(self, id):
        """
            This api help get advice job for student
        """
        user_repository = UserRepository()
        user = user_repository.get(id)
        if not user:
            abort(404, message=TranslationText.UserNotFound)
        user_sum_performance = self.user_performance_repository.get_sum_by_user(id)
        if not user_sum_performance:
            abort(400, message=TranslationText.PerformanceNotFound)
        list_performances = self.user_performance_repository.get_list_sum()
        df = pd.DataFrame(list_performances)
        performance_x = np.array([user_sum_performance[0].math, user_sum_performance[0].physics,
                                  user_sum_performance[0].chemistry, user_sum_performance[0].biology,
                                  user_sum_performance[0].literature, user_sum_performance[0].history,
                                  user_sum_performance[0].geography, user_sum_performance[0].phylosophy,
                                  user_sum_performance[0].art, user_sum_performance[0].foreign_language]).reshape(-1, 1)
        df['r2'] = df.apply(lambda row: self.calculate_r2(row, performance_x), axis=1)
        df = df.sort_values(by='r2', ascending=False)
        job_earning = self.get_list_job().json()
        job_earning_df = pd.DataFrame(job_earning, columns=['job', 'earn'])
        if df.empty:
            return {'jobs': list(job_earning_df.sort_values('earn', ascending=False).head(3)['job'])}
        match_jobs = self.get_3_jobs(list(df.iloc[:3].user_id))
        job_earning_df['job'] = job_earning_df['job'].str.lower()
        if match_jobs and len(match_jobs) >= 0:
            return {'job': match_jobs}
        else:
            return {'jobs': list(job_earning_df.sort_values('earn', ascending=False).head(3)['job'])}


class UserPostCurrentJobs(BaseResource):
    parser = reqparse.RequestParser()
    user_repository = UserRepository()
    user_performance_repository = UserSchoolPerformanceRepository()

    def post(self, id):
        """
            This api help input the current job for volunteer
        """
        user = self.user_repository.get(id)
        self.parser.add_argument('jobs', action='append', required=True, help=TranslationText.JobIsRequired)
        args = self.parser.parse_args()
        if not user:
            abort(404, message=TranslationText.UserNotFound)
        performances = self.user_performance_repository.get_by_user_id(id)
        if len(performances) == 0:
            abort(400, message=TranslationText.PleaseInputAtLeastOnePerformanceBeforeYouUpdateYourJob)

        user.jobs = args.get('jobs')
        self.user_repository.update(user)
        return user.to_dict()


api.add_resource(UserListAdd, '')
api.add_resource(UserRetrievedUpdate, '/<string:id>')
api.add_resource(UserListAddSchoolPerformance, '/<string:id>/school_performances')
api.add_resource(UserRetrieveUpdateSchoolPerformance, '/school_performances/<string:id>')
api.add_resource(UserGetAdviceJobs, '/<string:id>/advices')
api.add_resource(UserPostCurrentJobs, '/<string:id>/jobs')
