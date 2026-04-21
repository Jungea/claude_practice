from datetime import date
from sqlalchemy.orm import Session
from models import Todo


def get_todos(db: Session, status=None, priority=None):
    query = db.query(Todo)
    if status:
        query = query.filter(Todo.status == status)
    if priority:
        query = query.filter(Todo.priority == priority)
    return query.all()


def create_todo(db: Session, title: str, priority: str = "medium", due: str = None):
    todo = Todo(
        title=title,
        status="todo",
        priority=priority,
        due=due,
        created_at=date.today().isoformat(),
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update_status(db: Session, todo_id: int, status: str):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        return None
    todo.status = status
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        return None
    db.delete(todo)
    db.commit()
    return todo
