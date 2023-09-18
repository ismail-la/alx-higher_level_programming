#!/usr/bin/python3
""" This script defines a State class and a Base class
to work with MySQLAlchemy ORM.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class:
    Attributes:
        - __tablename__ (str): The name of the MySQL table
                               where state data is stored.
        - id (sqlalchemy.Integer): the state's id.
        - name (sqlalchemy.String): the state's name.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
