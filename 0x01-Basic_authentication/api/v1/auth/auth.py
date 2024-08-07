#!/usr/bin/env python3
"""the auth Module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """this is the auth class obj"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns True if the path requires authentication, False otherwise.

        :param path: The path to check
        :param excluded_paths: List of paths that do not require authentication
        :return: True if path requires authentication, False otherwise"""
        # If path is None, authentication is not required
        if path is None:
            return True
        # If excluded_paths is None or empty, authentication is required
        if excluded_paths is None or excluded_paths == []:
            return True
        # Normalize path by removing trailing slash
        path = path.rstrip('/')
        # Normalize path by removing trailing slash
        for excl_path in excluded_paths:
            # Normalize excluded_path by removing trailing slash
            excl_path = excl_path.rstrip('/')
            if path == excl_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """auth header method"""
        if request is None:
            return None
        # use the get method of the headers dictionary
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """finds current user"""
        return request
