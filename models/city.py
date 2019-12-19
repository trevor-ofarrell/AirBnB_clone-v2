#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False, primary_key=True)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
