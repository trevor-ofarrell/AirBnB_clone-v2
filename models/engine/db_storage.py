#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import MySQLdb
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

class DBStorage():
    
    __engine = None
    _session = None

    def __init__(self):
        """init method"""
        Session = sessionmaker()
        enginestr = "{}://{}:{}@{}:3306/{}".format(
            "mysql+mysqldb",
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB"))
        self.__engine = create_engine(enginestr, pool_pre_ping=True)
        Session.configure(bind=engine)
        session = Session()
        if getenv("HBNB_ENV") == 'test':
            session.drop_all()

    def all(self, cls=None):
        """return dict of all obj"""
        my_dict = {}
        if cls:
            q = self.__session.query(cls)
            my_dict.update({"{}.{}".format(cls, q.id): q})
        elif cls == None:
            q = self.__session.query().all()
            for queries in q:
                my_dict.update({"{}.{}".format(queries.__name__, queries.id): queries})

    def new(self, obj):
        """save new object to DB"""
        self.__session.add(obj)

    def save(self):
        """commit changes to DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from session"""
        session.delete(obj)
    
    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
