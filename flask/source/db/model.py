# Standard
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

#Custom
from . import db
from .. import config

Base = declarative_base()

class Roles(Base):
    __tablename__ = 'roles'
    team = Column(String, primary_key=True)
    role = Column(String, primary_key=True)
    created_at = Column(DateTime)