from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import url

engine = create_engine(url, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
