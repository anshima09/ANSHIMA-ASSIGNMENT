from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

# Database connection URL for PostgreSQL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine for database connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class for database sessions
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()

def get_db():
    """
    Dependency that provides a database session.
    Yields a session and ensures it is closed after use.
    """
    db = sessionLocal()
    try:
        yield db
    finally:
         db.close()