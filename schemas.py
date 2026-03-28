from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):

    username: str
    email: str
    password: str
    name: str


class UserUpdate(BaseModel):

    username: str
    email: str
    name: str
    password: str | None = None


class UserResponse(BaseModel):

    id: int
    username: str
    email: str
    name: str
    created_at: datetime

    class Config:
        from_attributes = True

