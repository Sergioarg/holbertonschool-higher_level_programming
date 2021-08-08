#!/usr/bin/python3
""" Mudole of class State from librarie of sqlalchemy """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.operators import ColumnOperators
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class City(Base):

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=False, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
