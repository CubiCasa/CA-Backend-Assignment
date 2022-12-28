import json
import os

import requests
from pydantic_models.jobs import JobPydantic


def find_job(job_name: str) -> JobPydantic:
    data = get_job_market_data()
    for job in data:
        if job_name == job[0]:
            return JobPydantic(
                name=job_name,
                salary=job[1],
            )
    return JobPydantic(
        name=job_name,
    )


def get_job_market_data():
    stat_site = os.environ.get('STAT_SITE')
    response = requests.get(stat_site + '/job_earnings')
    data = json.loads(response.content)
    return data


def encrypt_str(fernet, unencrypted_string):
    return fernet._encrypt_from_parts(
        unencrypted_string.encode(), 0,
        b'\xbd\xc0,\x16\x87\xd7G\xb5\xe5\xcc\xdb\xf9\x07\xaf\xa0\xfa',
    ).decode('ascii')
