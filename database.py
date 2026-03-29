import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Read from environment variables (set in Cloud Run)
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "Demo")
INSTANCE_CONNECTION_NAME = os.getenv("INSTANCE_CONNECTION_NAME")

# Cloud SQL Unix socket path (VERY IMPORTANT)
DB_HOST = f"/cloudsql/{INSTANCE_CONNECTION_NAME}"

# Final connection string (Cloud SQL format)
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}?host={DB_HOST}"

# Create engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # avoids stale connections
    pool_size=5,
    max_overflow=2
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()