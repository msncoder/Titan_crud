from fastapi import FastAPI
from app.api.todo import router as todo_router
from app.api.user import router as user_router
app = FastAPI()

app.include_router(todo_router)
app.include_router(user_router)


@app.get("/")
def home():
    return {
        "message":"hello"
    }