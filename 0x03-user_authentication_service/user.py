#!/usr/bin/env python3
"""the user Module"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """define class User which inherits from declarative base"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String)
    reset_token = Column(String)

    def __repr__(self):
        """string representation of the User object"""
        return "User(id={}, email={}, hashed_password={},\
            session_id={}, reset_token={})".format(self.id,
                                                   self.email,
                                                   self.hashed_password,
                                                   self.session_id,
                                                   self.reset_token)
