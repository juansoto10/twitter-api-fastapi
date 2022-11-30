# models.py
from models import UserBase, UserLogin, User, Tweet

# FastAPI
from fastapi import FastAPI
from fastapi import status
from typing import List


app = FastAPI()


# 1. Path Operations

# 1.1. Users

# Register user
@app.post(
    path='/signup',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary='Register a user',
    tags=['Users']
)
def signup():
    pass


# Login user
@app.post(
    path='/login',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Login a user',
    tags=['Users']
)
def login():
    pass


# Show all users
@app.get(
    path='/users',
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary='Show all users',
    tags=['Users']
)
def show_all_users():
    pass


# Show a user
@app.get(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Show a user',
    tags=['Users']
)
def show_user():
    pass


# Delete user
@app.delete(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Delete a user',
    tags=['Users']
)
def delete_user():
    pass


@app.put(
    path='/users/{user_id}',
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary='Update a user',
    tags=['Users']
)
def update_user():
    pass


# 1.2. Tweets

# Show all tweets
@app.get(
    path='/',
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary='Show all tweets',
    tags=['Tweets']
)
def home():
    return {'Twitter API': 'Working!'}


# Post tweet
@app.post(
    path='/post',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Post a tweet',
    tags=['Tweets']
)
def post():
    pass


# Show tweet
@app.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary='Show a tweet',
    tags=['Tweets']
)
def show_tweet():
    pass


# Delete tweet
@app.delete(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Delete a tweet',
    tags=['Tweets']
)
def delete_tweet():
    pass


# Update tweet
@app.put(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary='Update a tweet',
    tags=['Tweets']
)
def update_tweet():
    pass
