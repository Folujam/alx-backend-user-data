#!/usr/bin/env python3
"""authentication Module"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """method takes in a str and converts str into bytes,
    generates salt and hashes both
    param: password(a simple string should be passed)
    return: bytes(password and salt hashed)"""
    byte = password.encode('UTF-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(byte, salt)
    return hash


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ initializes Auth class"""
        self._db = DB()

    def register_user(email: str, password: str) -> User:
        """registers user if they dont exist"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))
