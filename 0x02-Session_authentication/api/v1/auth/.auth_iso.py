#!/usr/bin/env python3

"""
    Module - Auth
        A class to manage API authentication
"""

from flask import request
from typing import TypeVar, List


class Auth:
    """
    Manages API auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
         returns False - path and excluded_paths
         - assumes paths in excluded_paths contains '/' athe the end
        """
        if path and path[-1] != '/':
            path += '/'

        if excluded_paths and path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        returns None
        """
        if request:
            auth = request.headers.get('Authorization')
            if auth:
                return auth

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None
        """
        return None
