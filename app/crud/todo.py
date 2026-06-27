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


def get_todos(db:Session):
    return db.query(Todo).all()

def get_todo(db:Session,todo_id:int):
    return db.query(Todo).filter(
        Todo.id == todo_id
    ).first()
    


def update_todo(
        db:Session,
        todo_id:int,
        todo:TodoCreate
):
    todo_db = get_todo(db,todo_id)
    if not todo_db:
        return None
    todo_db.title = todo.title
    todo_db.description = todo.description

    db.commit()
    db.refresh(todo_db)

    return todo_db


def delete_todo(
        db:Session,
        todo_id:int
):
    db_todo = get_todo(db,todo_id)
    if not db_todo:
        return None
    
    db.delete(db_todo)
    db.commit()
    return db_todo
