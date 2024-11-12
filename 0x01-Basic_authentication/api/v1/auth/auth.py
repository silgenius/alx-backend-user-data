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
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns None
        """
        return None
