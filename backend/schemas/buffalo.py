
from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


class BuffaloCreate(BaseModel):
    tag_number: str = Field(min_length=1, max_length=30)
    name: str | None = None
    breed: str = Field(min_length=1)
    date_of_birth: date | None = None
    status: Literal["active", "sold"] = "active"


class BuffaloResponse(BuffaloCreate):
    id: str
    
