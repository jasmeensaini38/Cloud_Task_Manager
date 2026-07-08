# import create engine
from sqlalchemy import create_engine

# import sessionmaker
from sqlalchemy.orm import sessionmaker

# import declarative_base
from sqlalchemy.orm import declarative_base



DATABASE_URL='postgresql+psycopg2://neondb_owner:npg_9mHxM3sVFjGN@ep-late-butterfly-atckuphh-pooler.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
# here we connecting to a postgresql database hosted on the cloud

# note:click "show Password" and copy the completeconnection string

# create salalchemy engine
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

        
            

