from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Study(Base):
    __tablename__ = "studies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)


class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True)
    study_id = Column(Integer, ForeignKey("studies.id"))
    email = Column(String)
    code = Column(String)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    study_id = Column(Integer)
    text = Column(String)
    scale = Column(String)


class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True)
    participant_code = Column(String)
    question_id = Column(Integer)
    value = Column(Integer)
