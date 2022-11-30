# Python
import json
from typing import List

# models.py
from models import UserBase, UserLogin, User, Tweet, UserRegister

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body


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
def signup(user: UserRegister = Body(...)):
    """
    ## Sign up

    This path operation registers a user in the app and saves the information in the database.

    ### Parameters:

    - Request body parameter:

        - **user: UserRegister** -> A user model with user ID, email, first name, last name, birthdate and password.

    Returns a JSON with the basic user information:

        - user_id: UUID

        - email: EmailStr

        - first_name: str

        - last_name: str

        - birth_date: date
    """

    with open('users.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict['user_id'] = str(user_dict['user_id'])
        user_dict['birth_date'] = str(user_dict['birth_date'])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user


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


# Update user
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
