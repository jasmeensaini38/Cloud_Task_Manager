# import fastapi
from fastapi import FastAPI,Depends
# import base nd engine
from database import Base,engine,get_db
# import task table
from models import Task
from schemas import TaskSchema
from sqlalchemy.orm import Session
# connects to neon and ceck whther the tatasks table exists , if not then create it
Base.metadata.create_all(bind= engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome to cloud task manager API"}
# this api tells tht: FastAPI is running and the application started successfully

# now run the project uing uvicorn main:app reload


# asperday_2
# post method

@app.post("/create_task")
def create_task(task:TaskSchema,db: Session = Depends(get_db)):

    # create task object

    new_task = Task(task_title = task.task_title,description = task.description,assigned_to = task.assigned_to,priority = task.priority,status = task.status,due_date= task.due_date,created_by= task.created_by)


    # add task
    db.add(new_task)

    # db.commit
    db.commit()

    # refresh object 

    db.refresh(new_task)

    return {"message": "Task created Successfully"}

# the data sent from postman is first validated  by the taskschema (pydantic schema if it is valid the values
# are then copied into the tassk model , which responds database table and finally stored in the database)


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks
