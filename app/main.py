from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import People
from dotenv import dotenv_values
from .db import conn
from mongoengine import connect
from pymongo import MongoClient
import json

config = dotenv_values(".env")

app = FastAPI()
connect(db='db', host='localhost', port=27017, username='admin', password='admin')



@app.get('/')
def home():
    return {"message": "Hello World"}


@app.get('/get-all')
async def get_all():
    return {"test": 123}
