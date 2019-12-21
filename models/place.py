#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), nullable=False,
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False,
                             primary_key=True))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref='place',
                           cascade='all,delete,delete-orphan')
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship('Amenity',
                                 secondary='place_amenity', viewonly=False)
        reviews = relationship('Review',
                               backref='place',
                               cascade='all,delete,delete-orphan')
    else:
        @property
        def reviews(self):
            """getter attr"""
            l = []
            for items in models.storage.all(Review):
                if items.place_id == self.id:
                    l.append(items)
            return l

        @property
        def amenities(self):
            """getter attr"""
            l = []
            for items in models.storage.all(Amenity):
                if items.place_id == self.id:
                    l.append(items)
            return l

        @amenities.setter
        def amenities(self, obj):
            """setter"""
            if type(obj) == 'Amenity':
                self.amenity_ids.append(obj.id)
