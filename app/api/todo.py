
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.todo import TodoCreate,TodoResponse
from app.crud.todo import *
from app.api.user import get_current_user
from app.models.user import User

router = APIRouter(prefix="/todo",tags=["titan_todos"])

@router.post("/",response_model=TodoResponse)
def create(todo:TodoCreate,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return create_todo(db,todo,user_id=current_user.id)


@router.get('/')
def get_all(db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return get_todos(db, user_id=current_user.id)


@router.get("/{todo_id}",response_model=TodoResponse)
def get(todo_id:int,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    todo = get_todo(db,todo_id,user_id=current_user.id)
    if not todo:
        raise HTTPException(
            status=404,
            detail="Todo not found"
        )
    
    return todo

@router.put("/{todo_id}")
def update_todo_route(
    todo_id:int,
    todo:TodoCreate,
    db:Session=Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated = update_todo(db,todo_id,todo,user_id=current_user.id)
    if not updated:
        raise HTTPException(
            status=404,
            details = "Todo not Found"
        )
    return updated

@router.delete("/{todo_id}")
def delete(todo_id:int,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    deleted = delete_todo(
        db,todo_id, user_id=current_user.id
    )

    if not deleted:
        return HTTPException(
            status_code=404,
            status = "Todo not deleted"
        )
    
    return {
        "message": "Todo deleted successfully"
    }

