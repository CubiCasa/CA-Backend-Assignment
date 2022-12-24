from pydantic import BaseModel
from pydantic import Field


class Grade(BaseModel):
    math: float = Field(
        ge=0,
        le=10,
        description='Math score, base 10.',
    )
    physics: float = Field(
        ge=0,
        le=10,

        description='Physics score, base 10.',
    )
    chemistry: float = Field(
        ge=0,
        le=10,
        description='Chemistry score, base 10.',
    )
    biology: float = Field(
        ge=0,
        le=10,
        description='Biology score, base 10.',
    )
    literature: float = Field(
        ge=0,
        le=10,
        description='Literature score, base 10.',
    )
    history: float = Field(
        ge=0,
        le=10,
        description='History score, base 10.',
    )
    philosophy: float = Field(
        ge=0,
        le=10,
        description='Philosophy score, base 10.',
    )
    art: float = Field(
        ge=0,
        le=10,
        description='Art score, base 10.',
    )
    foreign_lang: float = Field(
        ge=0,
        le=10,
        description='Foreign Language score, base 10.',
    )
