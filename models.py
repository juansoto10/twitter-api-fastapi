# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional


# Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class UserBase(BaseModel):
    user_id: UUID = Field(
        ...,
        title='User ID',
    )
    email: EmailStr = Field(
        ...,
        title='Email',
        example='jeanneg@ntf.com'
    )


class PasswordMixin(BaseModel):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        title='Password',
        example='myfunnypassw0rd'
    )


class UserLogin(PasswordMixin, UserBase):
    pass


class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title='First name',
        example='Jeanne'
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title='Last name',
        example='Goursaud'
    )
    birth_date: Optional[date] = Field(
        default=None,
        title='Birthdate',
        example='1996-04-04'
    )


class UserRegister(PasswordMixin, User):
    pass


class Tweet(BaseModel):
    tweet_id: UUID = Field(
        ...,
        title='Tweet ID'
    )
    content: str = Field(
        ...,
        min_length=1,
        max_length=280,
        title='Tweet content'
    )
    created_at: datetime = Field(
        default=datetime.now(),
        title='Date and time of the tweet'
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        title='Date and time of the updated tweet'
    )
    created_by: User = Field(
        ...,
        title='Tweet author'
    )
