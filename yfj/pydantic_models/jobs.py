from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class JobPydantic(BaseModel):
    name: str = Field(
        description='Job name.',
    )
    salary: Optional[int] = Field(
        default=50000,
        description='Salary of this job',
    )


class InputJob(BaseModel):
    jobs: list[JobPydantic] = Field(
        min_items=1,
        description='List of jobs that user update about their career path. '
                    'Must have at least 1 job.',
    )


class Advices(BaseModel):
    advices: list[JobPydantic] = Field(
        max_items=3,
        min_items=3,
        description='List of 3 recommended jobs that our service returns to user.',
    )
