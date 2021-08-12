#!/usr/bin/python3
""" Module of class City from librarie of sqlalchemy with relationships """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    """ Empty class that inherits from Base """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
