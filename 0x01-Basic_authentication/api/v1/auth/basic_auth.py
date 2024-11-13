#!/usr/bin/env python3

"""
    Module: Basic auth
        Implements tthe basic authentication system
"""

from .auth import Auth
import base64
from models.user import User
from typing import TypeVar
import hashlib


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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """returns the decoded value of a Base64 string"""
        if base64_authorization_header:
            if isinstance(base64_authorization_header, str):
                try:
                    b64_value = base64.b64decode(base64_authorization_header)
                    # Decode from byte to str
                    b64_value = b64_value.decode('utf-8')
                except Exception:
                    pass
                else:
                    return b64_value
        return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header:
            if isinstance(decoded_base64_authorization_header, str):
                try:
                    name, pwd = decoded_base64_authorization_header.split(':')
                except Exception:
                    pass
                else:
                    return (name, pwd)
        return (None, None)

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
            ) -> TypeVar('User'):
        if user_email and user_pwd:
            if isinstance(user_email, str) and \
                    isinstance(user_pwd, str):
                users = User.search()
                if users and len(users) > 0:
                    for user in users:
                        user_pwd = hashlib.sha256(
                                user_pwd.encode()
                                ).hexdigest().lower()
                        if user.email == user_email \
                                and user._password == user_pwd:
                            return user
        return None
