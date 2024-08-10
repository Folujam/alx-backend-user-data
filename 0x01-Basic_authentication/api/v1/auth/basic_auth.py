#!/usr/bin/env python3
"""basic auth Module"""
Auth = __import__('auth').Auth


class BasicAuth(Auth):
    """this class inherits api/v1/auth/auth.py Auth class as base
    
        Extracts the Base64 part of the Authorization header for Basic Authentication.

        :param authorization_header: The Authorization header value
        :return: The Base64 encoded string, or None if invalid
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        base64_encoded = authorization_header[:6]
        return base64_encoded
