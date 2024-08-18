#!/usr/bin/env python3
"""authentication Module"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound
from typing import Union

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


def _generate_uuid() -> str:
    """returns a uuid str generated"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ initializes Auth class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """registers user if they dont exist"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """validates if password of user matches"""
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(password.encode('utf-8'),
                                      user.hashed_password)
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        """finds user by email, generates uuid,
        assigns session_id"""
        user = self._db.find_user_by(email=email)
        if user is None:
            return None
        ses_id = _generate_uuid()
        self._db.update_user(User.id, session_id=ses_id)
        return ses_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """finds user by session_id"""
        user_id = self._db.find_user_by(session_id=session_id)
        if session_id is None or user_id is None:
            return None
        return user_id
