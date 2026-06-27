from fastapi import FastAPI
from app.api.todo import router as todo_router

app = FastAPI()

app.include_router(todo_router)


@app.get("/")
def home():
    return {
        "message":"hello"
    }