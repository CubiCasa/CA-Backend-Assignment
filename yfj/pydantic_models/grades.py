import numpy as np
from pydantic import BaseModel
from pydantic import Field


class Grade(BaseModel):
    math: int = Field(
        ge=0,
        le=10,
        description='Math score, base 10.',
    )
    physics: int = Field(
        ge=0,
        le=10,

        description='Physics score, base 10.',
    )
    chemistry: int = Field(
        ge=0,
        le=10,
        description='Chemistry score, base 10.',
    )
    biology: int = Field(
        ge=0,
        le=10,
        description='Biology score, base 10.',
    )
    literature: int = Field(
        ge=0,
        le=10,
        description='Literature score, base 10.',
    )
    history: int = Field(
        ge=0,
        le=10,
        description='History score, base 10.',
    )
    philosophy: int = Field(
        ge=0,
        le=10,
        description='Philosophy score, base 10.',
    )
    art: int = Field(
        ge=0,
        le=10,
        description='Art score, base 10.',
    )
    foreign_lang: int = Field(
        ge=0,
        le=10,
        description='Foreign Language score, base 10.',
    )

    def avg_score(self) -> float:
        return (
            self.math + self.physics + self.chemistry + self.biology +
            self.literature + self.history + self.philosophy + self.art + self.foreign_lang
        ) / 9

    def get_list_score(self) -> np.array:
        return np.array([
            self.math, self.physics, self.chemistry, self.biology,
            self.literature, self.history, self.philosophy, self.art, self.foreign_lang,
        ])
