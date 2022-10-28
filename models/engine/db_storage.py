#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Class for DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        usr = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        env = os.getenv('HBNB_MYSQL_ENV')
        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(usr, pwd, host, db)

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """return all objects in DBStorage session"""
        classes = ["User", "State", "City", "Place", "Amenity", "Review"]
        new_dict = {}

        if cls is None:
            obj_list = []

            for cls in classes:
                obj_list.extend(self.__session.query(cls).all())
            for obj in obj_list:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj

        else:
            for obj in self.__session.query(DBStorage.classes[cls].all()):
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj

        return new_dict

    def new(self, obj):
        """add new object to DBStorage session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to DBStorage session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete instance in DBStorage session"""
        if obj is None:
            return
        else:
            self.__session.delete(obj)

    def reload(self, obj=None):
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))
