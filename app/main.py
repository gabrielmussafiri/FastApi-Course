

from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from . import models ,schemas
from .database import engine ,get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, HTTPException, Depends , APIRouter
from .database import engine ,get_db
from sqlalchemy.orm import Session
from .routers import post , user ,auth
from fastapi import FastAPI, Response, status, HTTPException, Depends , APIRouter



models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    
# Connection to the Database Postgres Using Psycopg2
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='gm', password='Yannick1988',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print('connection to the database failed')
#         print('Error: ',error)
#         time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Welcome to my API!"}
