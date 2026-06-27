from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.todo import TodoCreate,TodoResponse
from app.crud.todo import *


router = APIRouter(prefix="/todo",tags=["titan_todos"])

@router.post("/",response_model=TodoResponse)
def create(todo:TodoCreate,db:Session=Depends(get_db)):
    return create_todo(db,todo)