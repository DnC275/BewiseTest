import dateutil.parser

from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, validator


class QuestionBase(BaseModel):
    question: str
    answer: str
    created_at: date
    # added_at: Optional[datetime]

    class Config:
        orm_mode = True

    @validator('created_at', pre=True)
    def validate_date(cls, created_at):
        if type(created_at) == str:
            return dateutil.parser.isoparse(created_at).date()
        return created_at


class QuestionDB(QuestionBase):
    id: int


class GetQuestionRequest(BaseModel):
    questions_num: int
