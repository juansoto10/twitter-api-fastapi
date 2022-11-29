# models.py
from models import UserBase, UserLogin, User, Tweet

# FastAPI
from fastapi import FastAPI


app = FastAPI()


@app.get(path='/')
def home():
    return {'Twitter API': 'Working!'}
