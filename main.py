from fastapi import FastAPI , Request
from fastapi.templating import Jinja2Templates

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
    