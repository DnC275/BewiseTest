from typing import List

import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, BackgroundTasks

from questions import models, schemas
from questions.database import engine
from questions.repositories import QuestionsRepository
from pydantic import parse_obj_as

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/questions/", response_model=schemas.QuestionBase)
def generate_questions(data: schemas.GetQuestionRequest, background_tasks: BackgroundTasks, questions: QuestionsRepository = Depends()):
    question = questions.get_last()
    background_tasks.add_task(questions.generate, data.questions_num)
    return question


# @app.get("/questions/", response_model=List[schemas.QuestionBase])
# def generate_questions(questions: QuestionsRepository = Depends()):
#     questions = questions.all()
#     return parse_obj_as(List[schemas.QuestionBase], questions)
#
#
# @app.get("/questions/last/", response_model=schemas.QuestionBase)
# def get_last(questions: QuestionsRepository = Depends()):
#     question = questions.get_last()
#     return schemas.QuestionBase.from_orm(question)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
