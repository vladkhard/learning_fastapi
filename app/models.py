from typing import Optional

from pydantic import BaseModel, ValidationError, validator


SEXES = [
    "male",
    "female",
]

DEFAULT_USER = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 42,
}


class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    sex: Optional[str]

    @validator("age")
    def age_in_range(cls, value):
        if value < 0 or value > 99:
            raise ValidationError("age is out of bounds")
        return value

    @validator("sex")
    def sex_is_one_of_selection(cls, value):
        value = value.lower()
        if value not in SEXES:
            raise ValidationError("sex is not recognized")
        return value
