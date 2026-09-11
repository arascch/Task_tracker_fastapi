from fastapi import FastAPI , Request , Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlmodel import Session , select
from models import Task
from database import engine

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
    return templates.TemplateResponse(
        request=request , name="index.html" , context={"tasks":tasks}
    )

@app.post("/add")
def add_task(task_title:str=Form(...)):
    with Session(engine) as session:
        new_task = Task(title=task_title)
        session.add(new_task)
        session.commit()
    return RedirectResponse(url="/" , status_code=303)

@app.post("/delete/{task_id}")
def delete_task(task_id : int):
    with Session(engine) as session:
        task = session.get(Task , task_id)
        if task : 
            session.delete(task)
            session.commit()
    return RedirectResponse(url="/" , status_code=303)

@app.post("/update/{task_id}")
def update_task(task_id:int):
    with Session(engine) as session:
        task = session.get(Task, task_id)

        if task : 
            task.completed = not task.completed

            session.add(task)
            session.commit()
    return RedirectResponse(url="/" , status_code=303)