# Standard
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Custom
from .. import config
from .model import Base, Roles

def getDBConnection(database):
    engine = create_engine(f'postgresql://{config.dbUser}:{config.dbPassword}@postgres/{database}')
    return engine

def getSession(engine):
    Session = sessionmaker(engine)
    session = Session()
    return session

def insertData(engine, objectInstance):
    Session = sessionmaker(engine)
    session = Session()
    session.add(objectInstance)
    session.commit()

def exeStatement(engine, statement):
    session = sessionmaker()
    session.configure(bind=engine)
    session().execute(statement)

def initializeDatabase(engine):
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
