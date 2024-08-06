#!/usr/bin/env python3
"""the auth Module"""
from flask import request
from typing import List, TypeVar

class Auth:
    """this is the auth class obj"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth method"""
        pass


    def authorization_header(self, request=None) -> str:
        """auth header method"""
        return request
    

    def current_user(self, request=None) -> TypeVar('User'):
        """finds current user"""
        return request
