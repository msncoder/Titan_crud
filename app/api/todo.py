from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.todo import TodoCreate,TodoResponse
from app.crud.todo import *


router = APIRouter(prefix="/todo",tags=["titan_todos"])

@router.post("/",response_model=TodoResponse)
def create(todo:TodoCreate,db:Session=Depends(get_db)):
    return create_todo(db,todo)


@router.get('/')
def get_all(db:Session=Depends(get_db)):
    return get_todos(db)


@router.get("/{todo_id}",response_model=TodoResponse)
def get(todo_id:int,db:Session=Depends(get_db)):
    todo = get_todo(db,todo_id)
    if not todo:
        raise HTTPException(
            status=404,
            detail="Todo not found"
        )
    
    return todo

@router.put("/{todo_id}")
def update(
    todo_id:int,
    todo:TodoCreate,
    db:Session=Depends(get_db)
):
    updated = update(db,todo_id,todo)
    if not updated:
        raise HTTPException(
            status=404,
            details = "Todo not Found"
        )