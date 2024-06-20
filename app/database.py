# Creating database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define SQLite database URL
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# Create SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# Create Session for database 
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# Declering Base class for ORM models 
Base = declarative_base()

# get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
