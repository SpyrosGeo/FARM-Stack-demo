# from typing import Optional

from model import Todo
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import(
    fetch_all_todos, fetch_one_todo, remove_todo, update_todo,create_todo,
)

app = FastAPI()

origins = ['https://localhost:3000']
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo{title}",response_model=Todo)
async def get_todo_by_id(title):
    response = await get_todo_by_id(title)
    if response:
        return response
    raise HTTPException(404,f"Could not find title {title}")


@app.post("/api/todo",response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return "Succesfully deleted Todo item"
    raise HTTPException(400,"Something went wrong")



@app.put("/api/todo{title}",response_model=Todo)
async def put_todo(title:str, desc:str):
    response = await update_todo(title,desc)
    if response:
        return response
    raise HTTPException(404,f"No todo item with the title {title}")


@app.delete("/api/todo{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
         return response
    raise HTTPException(404,f"No todo item with the title {title}")
