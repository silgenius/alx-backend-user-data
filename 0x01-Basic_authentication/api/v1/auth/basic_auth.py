#!/usr/bin/env python3

"""
    Module: Basic auth
        Implements tthe basic authentication system
"""

from .auth import Auth


class BasicAuth(Auth):
    """
    Implements tthe basic authentication system
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """returns the Base64 part of the Authorization header"""
        if authorization_header:
            if isinstance(authorization_header, str):
                try:
                    auth_value = authorization_header.split()
                except Exception:
                    pass
                else:
                    if auth_value[0] == 'Basic':
                        return auth_value[1]
        return None
