from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, index=True)

    email = Column(String(150), unique=True)

    password = Column(String)

    name = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

