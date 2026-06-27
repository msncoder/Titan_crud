from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate,TodoResponse


def create_todo(db:Session,todo:TodoCreate):
    db_todo = Todo(
        title = todo.title,
        description = todo.description
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
