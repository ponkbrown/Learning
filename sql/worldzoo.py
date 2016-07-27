# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class World(Base):
    __tablename__ = 'world'

    name = Column(String(50), primary_key=True)
    continent = Column(String(60))
    area = Column(Numeric(10))
    population = Column(Numeric(11))
    gdp = Column(Numeric(14))
    capital = Column(String(60))
    tld = Column(String(5))
    flag = Column(String(255))

engine = create_engine('sqlite:///worldzoo.db')
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
