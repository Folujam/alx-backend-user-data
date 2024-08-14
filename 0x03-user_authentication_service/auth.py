#!/usr/bin/env python3
"""authentication Module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """method takes in a str and converts str into bytes,
    generates salt and hashes both
    param: password(a simple string should be passed)
    return: bytes(password and salt hashed)"""
    byte = password.encode('UTF-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(byte, salt)
    return hash
