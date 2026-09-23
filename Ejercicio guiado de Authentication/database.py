from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

DB_URI = 'postgresql://postgres:Gorro220394@localhost:5432/postgres'
engine = create_engine(DB_URI, echo=True)

Session = sessionmaker(bind=engine)