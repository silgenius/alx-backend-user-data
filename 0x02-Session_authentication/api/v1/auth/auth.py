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
        if path is None:
            return True

        if not excluded_paths:
            return True

        # Normalize the path by removing any trailing slashes
        normalized_path = path.rstrip('/')

        # Iterate over excluded paths
        for excluded in excluded_paths:
            # Normalize the excluded path by removing trailing slashes
            normalized_excluded = excluded.rstrip('/')

            # Check for wildcard '*' at the end of excluded path
            if normalized_excluded.endswith('*'):
                # Remove '*' and check if the path starts with the prefix
                prefix = normalized_excluded[:-1]
                if normalized_path.startswith(prefix):
                    return False
            else:
                # If no wildcard, compare exactly
                if normalized_path == normalized_excluded:
                    return False

        # If path is not in the excluded paths, return True
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
