""" This module contains the 'index' Blueprint which organize and
group, views related to the index endpoint of HTTP REST API.
"""

from flask import Blueprint
from flask_restful import Api, Resource, url_for

bp = Blueprint('index', __name__, url_prefix='')
api = Api(bp)


class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}


api.add_resource(TodoItem, '/todos/<int:id>')
