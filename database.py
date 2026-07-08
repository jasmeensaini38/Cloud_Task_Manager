# import create engine
from sqlalchemy import create_engine

# import sessionmaker
from sqlalchemy.orm import sessionmaker

# import declarative_base
from sqlalchemy.orm import declarative_base

# as per day2
import os
from dotenv import load_dotenv
load_dotenv()
# import the function that can read a .env file,i.e open the .env file and load all its variables 
# into the memory

DATABASE_URL=os.getenv("DATABASE_URL")
# here we connecting to a postgresql database hosted on the cloud

# note:click "show Password" and copy the completeconnection string

# create salalchemy engineo
# the engine is responsible for creting fastapi with the cloud PostgreSQL

engine = create_engine(DATABASE_URL)

# CReate session asa every database operation will 

SessionLocal = sessionmaker(bind= engine)

Base = declarative_base()

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()

        
            

