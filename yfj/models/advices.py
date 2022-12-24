from pydantic import BaseModel
from pydantic import Field


class Job(BaseModel):
    name: str = Field(
        description='Job name.',
    )


class InputJob(BaseModel):
    jobs: list[Job] = Field(
        min_items=1,
        description='List of jobs that user update about their career path. '
                    'Must have at least 1 job.',
    )


class Advices(BaseModel):
    advices: list[Job] = Field(
        max_items=3,
        min_items=3,
        description='List of 3 recommended jobs that our service returns to user.',
    )
