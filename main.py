from fastapi import FastAPI , Depends, HTTPException 
from schemas import Todo as TodoSchema, Todocreate 
from sqlalchemy.orm import Session
from database import sessionlocal
from models import Todo
from database import base, engine

base.metadata.create_all(bind=engine)

app=FastAPI() 

def get_db() : 
    db=sessionlocal() 
    try : 
        yield db 
        
    finally : 
        db.close()

@app.post("/todos",response_model=TodoSchema) 
def create (todo:Todocreate, db:Session=Depends(get_db)): 
    db_todo=Todo(**todo.dict())
    db.add(db_todo) 
    db.commit() 
    db.refresh(db_todo) 
    return db_todo 


@app.get("/todos",response_model=list[TodoSchema]) 
def read_todos (db:Session=Depends(get_db)) : 
    return db.query(Todo).all()

@app.get("/todos/{todo_id}",response_model=TodoSchema) 
def read_todo(todo_id:int,db:Session=Depends(get_db)) : 
    todo=db.query(Todo).filter(Todo.id==todo_id).first() 
    if not todo: 
        raise HTTPException(status_code=404,detail="ID not found") 
    return todo  

@app.put("/todos/{todo_id}",response_model=TodoSchema) 
def update_todo(todo_id:int,updated:Todocreate,db:Session=Depends(get_db)) : 
    todo=db.query(Todo).filter(Todo.id==todo_id).first() 
    if not todo: 
        raise HTTPException(status_code=404,detail="ID not found") 
    for key,values in updated.dict().items() : 
        setattr(todo,key,values) 
    db.commit() 
    db.refresh(todo) 
    return todo 

@app.delete("/todos/{todo_id}") 
def delete_todo(todo_id:int,db:Session=Depends(get_db)) : 
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo: 
        raise HTTPException(status_code=404,detail="ID not found")  
    db.delete(todo) 
    db.commit() 
    return {"message":f"{todo_id} successfully deleted"}