#Database connection and setup using SQLAlchemy and environment variables for configuration.

from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker, declarative_base; 
from dotenv import load_dotenv 
import os 

load_dotenv() 
DATABASE_URL=os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL) 
sessionlocal=sessionmaker(bind=engine,autoflush=False)
base=declarative_base() 