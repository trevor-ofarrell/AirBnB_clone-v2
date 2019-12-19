#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from os import getenv


class DBStorage():

    __engine = None
    __session = None

    def __init__(self):
        """init method"""
        enginestr = "{}://{}:{}@{}:3306/{}".format(
            "mysql+mysqldb",
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB"))
        self.__engine = create_engine(enginestr, pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            session.drop_all()

    def all(self, cls=None):
        """Show all class objects in DBStorage or specified class if given
        """
        if cls:
            query = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place]
            query = []
        for item in classes:
            query += self.__session.query(item)
        my_dict = {}
        for obj in query:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """save new object to DB"""
        self.__session.add(obj)

    def save(self):
        """commit changes to DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from session"""
        self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
