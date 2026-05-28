#Data validation, parsing, serialization, error message generation
from typing import Optional 
from pydantic import BaseModel 

class Todobase(BaseModel) : 
    
    title: str
    description: Optional[str] = None  
    completed: bool = False
    
class Todocreate(Todobase) : 
    pass 

class Todo(Todobase) : 
    
    id: int 
    class Config: 
        orm_mode=True 
                