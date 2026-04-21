from sqlalchemy import Column, Integer, String, Date
from db import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    status = Column(String, default="todo")       # todo / in_progress / done
    priority = Column(String, default="medium")   # high / medium / low
    due = Column(String, nullable=True)
    created_at = Column(String, nullable=False)
