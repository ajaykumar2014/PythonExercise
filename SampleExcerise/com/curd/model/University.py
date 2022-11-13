from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy import engine
from sqlalchemy.ext.declarative import declarative_base

engine = client = create_engine('sqlite:///university_lite_store.db',echo=True)
Base = declarative_base()

class University(Base):
    __tablename__ = 'universityTable'
    index = Column(Integer,primary_key='True',autoincrement=True)
    name = Column(String)
    country = Column(String)
    Domains = Column(String)
    WebPages = Column(String)
