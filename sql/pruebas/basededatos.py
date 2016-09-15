# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import scoped_session, sessionmaker, Query

engine = create_engine('sqlite:///worldzoo.db')
Base = declarative_base()
Base.metadata.reflect(engine
)
class World(Base):
    __table__ = Base.metadata.tables['world']

db_session = scoped_session(sessionmaker (bind=engine))

for item in db_session.query(World.name):
    print(item)
