import logging

from .database import Base, SessionLocal, engine
from .models import ChartData

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Insert dummy data
session = SessionLocal()
try:
    data = [ChartData(name=f"Point {i}", value=i * 10) for i in range(1, 6)]
    session.add_all(data)
    session.commit()
    logging.info("Database created and dummy data inserted successfully!")
except BaseException:
    session.rollback()
    logging.exception("An error occurred: %s")
finally:
    session.close()

logging.info("Database created and dummy data inserted successfully!")
