# import Basemodel
from pydantic import BaseModel

# task creation schema
class TaskSchema(BaseModel):

    # task_title
    task_title : str
    # task description
    description : str

    # assignedto
    
    assigned_to :str
    
    priority : str

    status: str

    due_date  :str

    created_by : str

