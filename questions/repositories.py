import requests
import logging

from typing import List

from fastapi.params import Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc

from .models import Question
from .dependencies import get_db
from .schemas import QuestionDB


EXTERNAL_API_URL = 'https://jservice.io/api/random?count={}'


logger = logging.getLogger(__name__)


class QuestionsRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find(self, id: int) -> Question:
        query = self.db.query(Question)
        return query.filter(Question.id == id).first()

    def get_last(self) -> Question:
        query = self.db.query(Question)
        return query.order_by(desc(Question.added_at)).first()

    def all(self) -> List[Question]:
        query = self.db.query(Question)
        return query.all()

    def generate(self, count: int) -> None:
        print(count)
        response_data = self._get_questions_request(count)
        for question_data in response_data:

            if self.find(question_data['id']) is not None:
                continue

            question = QuestionDB(**question_data)
            question_db_model = Question(**dict(question))
            self.db.add(question_db_model)
            self.db.commit()
            count -= 1

        if count == 0:
            return
        self.generate(count)

    def _get_questions_request(self, count: int, attempts=20):
        url = EXTERNAL_API_URL.format(count)
        response = requests.request(method='get', url=url)
        if response.status_code != 200:
            if attempts > 0:
                logger.info(f'Retrieved questions failed, Response status: {response.status_code}, Response data: {response.json}')
                return self._get_questions_request(count, attempts=attempts-1)
            else:
                raise Exception("Question service doesn't work or request is invalid")
        return response.json()
