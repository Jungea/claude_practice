from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import engine, Base, get_db
import models, crud
from schemas import TodoCreate, TodoResponse
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/todos", response_model=List[TodoResponse])
def list_todos(status: str = None, priority: str = None, db: Session = Depends(get_db)):
    return crud.get_todos(db, status=status, priority=priority)


@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, title=todo.title, priority=todo.priority, due=todo.due)


@app.patch("/todos/{todo_id}/status", response_model=TodoResponse)
def update_status(todo_id: int, status: str, db: Session = Depends(get_db)):
    result = crud.update_status(db, todo_id, status)
    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")
    return result


@app.delete("/todos/{todo_id}", response_model=TodoResponse)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    result = crud.delete_todo(db, todo_id)
    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")
    return result
