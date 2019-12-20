#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import MySQLdb
from sqlalchemy.orm import relationship, backref

DBSession = scoped_session(sessionmaker())


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", cascade="all,delete,delete-orphan", backref='state')

    @property
    def cities(self):
        """getter method"""
        q = []
        for items in models.storage.all(City):
            if items.state_id == self.id:
                q.append(items)
        return q
