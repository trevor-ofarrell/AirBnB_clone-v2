#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenitites"
    name = Column(String(128), nullable=False)
