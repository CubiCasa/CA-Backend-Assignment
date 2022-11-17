import json

from flask import make_response
from flask_restful import Api


def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    if code in [200, 201, 202]:
        resp = make_response(json.dumps(dict(data=data, status=True, message=data.get('message') if data else '')),
                             code)
    else:
        resp = make_response(json.dumps(dict(data=None, status=False, message=data.get('message') if data else '')),
                             code)
    resp.headers.extend(headers or {})
    return resp


class CustomApi(Api):
    def __init__(self, *args, **kwargs):
        super(CustomApi, self).__init__(*args, **kwargs)
        self.representations = {
            'application/json': output_json,
        }
