from fastapi import FastAPI , Request , Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

tasks = [
    {"id":1 , "title":"learn Fastapi" , "completed" : False},
    {"id":2 , "title":"learn tailwind", "completed" : False}
]

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        request= request,
        name = "index.html",
        context={"task":tasks}
    )

@app.post("/add")
def add_task(task_title:str=Form(...)):
    new_id = len(tasks) + 1
    tasks.append({"id":new_id , "title":task_title , "completed":False})
    return RedirectResponse(url="/" , status_code=303)

@app.post("/delete/{task_id}")
def delete_task(task_id : int):
    global tasks

    tasks = [task for task in tasks if task["id"]!=task_id]
    return RedirectResponse(url="/", status_code=303)