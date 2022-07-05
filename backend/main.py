from fastapi import FastAPI, status, HTTPException, Depends, Response
from database import Base, engine, SessionLocal
import models
import schemas
from typing import List
from sqlalchemy.orm import Session
from tasks import create_pdf_task
from fastapi.responses import FileResponse
import os
import pathlib


Base.metadata.create_all(engine)


app = FastAPI()


def create_static_folder():
    try:
        pathlib.Path(f"{os.getcwd()}/static").mkdir()
    except:
        pass


create_static_folder()
create_pdf_task.delay()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/")
def root():
    return "todooo"


@app.get("/todo/file")
def get_pdf_file():
    return FileResponse(path="static/data_pdf.pdf")


@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoCreate, session: Session = Depends(get_session)):
    tododb = models.ToDo(task=todo.task)

    session.add(tododb)
    session.commit()
    session.refresh(tododb)

    create_pdf_task.delay()
    return tododb


@app.get("/todo/{id}", response_model=schemas.ToDo)
def read_todo(id: int, session: Session = Depends(get_session)):
    todo = session.query(models.ToDo).get(id)

    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo


@app.put("/todo/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_todo(id: int, task: str, session: Session = Depends(get_session)):
    todo = session.query(models.ToDo).get(id)
    if todo:
        todo.task = task
        session.commit()

    if not todo:
        raise HTTPException(status_code=404, detail=f"todo with item id {id} not found")
    create_pdf_task.delay()
    return todo

@app.put("/todo/{id}/done", status_code=status.HTTP_202_ACCEPTED)
def update_todo(id: int, done: bool, session: Session = Depends(get_session)):
    todo = session.query(models.ToDo).get(id)
    if todo:
        todo.done = done
        session.commit()

    if not todo:
        raise HTTPException(status_code=404, detail=f"todo with item id {id} not found")
    create_pdf_task.delay()
    return todo
   


@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_todo(id: int, session: Session = Depends(get_session)):
    todo = session.query(models.ToDo).get(id)

    if todo:
        session.delete(todo)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    create_pdf_task.delay()
    return None


@app.get("/todo", response_model=List[schemas.ToDo])
def read_todo_list(session: Session = Depends(get_session)):
    todo_list = session.query(models.ToDo).all()

    return todo_list
