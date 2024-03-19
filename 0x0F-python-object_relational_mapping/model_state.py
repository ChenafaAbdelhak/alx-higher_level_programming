#!/usr/bin/python3
"""
defines a State class and an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mmetadata = MetaData()
Base = declarative_base(metadata=mmetadata)


class State(Base):
    """State class with id and name attributes"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
