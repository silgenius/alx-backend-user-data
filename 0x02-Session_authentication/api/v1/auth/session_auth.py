#!/usr/bin/env python3

"""
    Module - Auth
        A class to manage API authentication
"""

from flask import request
from typing import TypeVar, List
from .auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    Implement the session authentication system
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id:
            if isinstance(user_id, str):
                session_id = str(uuid.uuid4())
                self.user_id_by_session_id[session_id] = user_id
                return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID
        """
        if session_id:
            if isinstance(session_id, str):
                return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """
        returns a User instance based on a cookie value
        """
        session_id = self.session_cookie(request)
        if session_id:
            user_id = self.user_id_for_session_id(session_id)
            user = User.get(user_id)
            if user:
                return user
        return None

    def destroy_session(self, request=None):
        """
        deletes the user session / logout
        """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                user_id = self.user_id_for_session_id(session_id)
                if user_id:
                    self.user_id_by_session_id.pop(session_id)
                    return True
        return False
