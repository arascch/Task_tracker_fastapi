from sqlmodel import create_engine , SQLModel
from models import Task

engine = create_engine("sqlite///tasks.db")

SQLModel.metadata.create_all(engine)