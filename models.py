# import required sqlalchemy columns
from sqlalchemy import Column,Integer,String

# import base class
from database import Base

# create task  table
class Task(Base):

    # TABLename
    __tablename__ = "tasks"

    # primary kaey
    id = Column(Integer,primary_key=True)

    # task title
    task_title = Column(String, nullable = False)

    # task description

    description = Column(String)

    assigned_to = Column(String)

    priority = Column(String)

    status = Column(String)

    due_date= Column(String)

    created_by = Column(String)

    



