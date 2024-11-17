#!/usr/bin/env python3

"""
    Module - Auth
        A class to manage API authentication
"""

from .session_exp_auth import SessionExpAuth
import json
from datetime import datetime
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    Implement session DB
    """
    filename = 'session_dictionary'
    user_id_by_session_id = {}

    def __init__(self):
        """
        Initialize session db auth
        """
        super().__init__()

    def create_session(self, user_id=None):
        """
        creates a session id by calling create_session()
        and add to file
        """
        session_id = super().create_session(user_id)
        if session_id:
            user_session = UserSession(user_id, session_id)
            user_session.save()
            return session_id
        return session_id

    def destroy_session(self, request=None):
        """
        deletes the user session / logout
        """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                user = UserSession.search({'session_id': session_id})
                if len(user) > 0:
                    user[0].remove()

    def user_id_for_session_id(self, session_id=None):
        """
         returns the User ID by requesting UserSession in the
         database based on session_id
        """
        if session_id:
            user = UserSession.search({'session_id': session_id})
            if len(user) > 0:
                return super().user_id_for_session_id(user[0].session_id)
        return None
