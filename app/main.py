from fastapi import FastAPI
from .models import People
from dotenv import dotenv_values
from .db import conn
from mongoengine import connect
from pymongo import MongoClient
import json

config = dotenv_values(".env")

app = FastAPI()
connect(db='db', host='localhost', port=27017, username='admin', password='admin')

@app.on_event("startup")
def startup_db_client():
    print("========")
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]


@app.get('/')
def home():
    return {"message": "Hello World"}


@app.get('/get-all')
async def get_all():
    print("--------")
    conn.local.user.find()
    print(conn.local.user.find())
    return {"test": 123}
