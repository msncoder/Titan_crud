
from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate

# Yahan humne user_id ko add kiya hai parameter me
def create_todo(db: Session, todo: TodoCreate, user_id: int):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        user_id=user_id  # Database me user_id save ho rahi hai
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


# Sirf us user ke todos lane ke liye jo logged-in hai
def get_todos(db: Session, user_id: int):
    return db.query(Todo).filter(Todo.user_id == user_id).all()


# Kisi specific todo ko sirf uske owner ke liye fetch karne ke liye
def get_todo(db: Session, todo_id: int, user_id: int):
    return db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == user_id
    ).first()


# Apne todo ko update karne ke liye
def update_todo(db: Session, todo_id: int, todo: TodoCreate, user_id: int):
    todo_db = get_todo(db, todo_id, user_id)
    if not todo_db:
        return None
    todo_db.title = todo.title
    todo_db.description = todo.description

    db.commit()
    db.refresh(todo_db)
    return todo_db


# Apne todo ko delete karne ke liye
def delete_todo(db: Session, todo_id: int, user_id: int):
    db_todo = get_todo(db, todo_id, user_id)
    if not db_todo:
        return None
    
    db.delete(db_todo)
    db.commit()
    return db_todo

