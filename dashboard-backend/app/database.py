import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Create the database engine
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
else:
    engine = create_engine(DATABASE_URL)

Base = declarative_base()

# Create all tables in the database
Base.metadata.create_all(bind=engine)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine),
)


def get_db():
    """
    Dependency that provides a SQLAlchemy session.

    Yields
    ------
        db (SessionLocal): SQLAlchemy session object.

    Usage:
        Use this function as a dependency in your route functions to get a
        database session.

    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
