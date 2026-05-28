#Table creation for todo app using sqlalchemy

from sqlalchemy import Column, Integer, String, Boolean 
from database import base 

class Todo(base) : 
    
    __tablename__="todos" 
    id=Column(Integer,primary_key=True,index=True) 
    title=Column(String,nullable=False) 
    description=Column(String) 
    completed=Column(Boolean,default=False)  
    