import json
import logging
import os

import requests

logger = logging.getLogger(__name__)


class ApiException(Exception):
    pass


class ApiClient:
    def __init__(self, api_url=os.environ.get('STATS_URL'), api_key='', session_key=''):
        self.session = requests.session()
        self.session.headers = {'Content-type': 'application/json',
                                'X-Authorization': 'Bearer ' + session_key}
        self.api_url = api_url
        self.api_key = api_key

    def post(self, url, data):
        for retries in range(3):
            try:
                url = self.api_url + url
                if self.api_key:
                    data['apiKey'] = self.api_key
                r = self.session.post(url=url, data=json.dumps(data))
                if r.ok:
                    return r
                else:
                    raise ApiException("Api {} return error code {} and text {} ".format(url, r.status_code, r.text))
            except (requests.Timeout, requests.ConnectionError,) as e:
                logger.warning("Api {} retries after timeout {}".format(url, e))
                continue

        raise ApiException("Api {} failed after reach to max retries !".format(url))

    def get(self, url):
        for retries in range(3):
            try:
                url = self.api_url + url
                r = self.session.get(url=url)
                if r.ok:
                    return r
                else:
                    raise ApiException("Api {} return error code {} and text {} ".format(url, r.status_code, r.text))
            except (requests.Timeout, requests.ConnectionError,) as e:
                logger.warning("Api {} retries after timeout {}".format(url, e))
                continue

        raise ApiException("Api {} failed after reach to max retries !".format(url))

    def put(self, url, data):
        for retries in range(3):
            try:
                url = self.api_url + url
                if self.api_key:
                    data['apiKey'] = self.api_key
                r = self.session.put(url=url, data=json.dumps(data))
                if r.ok:
                    return r
                else:
                    raise ApiException("Api {} return error code {} and text {} ".format(url, r.status_code, r.text))
            except (requests.Timeout, requests.ConnectionError,) as e:
                logger.warning("Api {} retries after timeout {}".format(url, e))
                continue

        raise ApiException("Api {} failed after reach to max retries !".format(url))

    def delete(self, url):
        for retries in range(3):
            try:
                url = self.api_url + url
                r = self.session.delete(url=url)
                if r.ok:
                    return r
                else:
                    raise ApiException("Api {} return error code {} and text {} ".format(url, r.status_code, r.text))
            except (requests.Timeout, requests.ConnectionError,) as e:
                logger.warning("Api {} retries after timeout {}".format(url, e))
                continue

        raise ApiException("Api {} failed after reach to max retries !".format(url))
