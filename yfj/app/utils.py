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
