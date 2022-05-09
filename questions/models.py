from sqlalchemy import Column, Integer, String, Date, DateTime, func
from questions.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(512))
    answer = Column(String(128))
    created_at = Column(Date)
    added_at = Column(DateTime, server_default=func.now())
