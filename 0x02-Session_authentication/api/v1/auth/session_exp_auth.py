#!/usr/bin/env python3

"""
Module
    SessionExpAuth - Implements session expiration for
    SessionAuth system
"""

from api.v1.auth.session_auth import SessionAuth
from models.user import User
from datetime import (datetime, timedelta)
import os


class SessionExpAuth(SessionAuth):
    """
    Manages expiration for session auth
    """
    user_id_by_session_id = {}

    def __init__(self):
        self.session_duration = os.getenv('SESSION_DURATION')
        try:
            self.session_duration = int(self.session_duration)
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        creates a session id by calling create_session()
        """
        session_id = super(SessionExpAuth, self).create_session(user_id)
        if not session_id:
            return None

        session_dictionary = {
                'user_id': user_id,
                'created_at': datetime.now()
                }
        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        returns user session if not yet expire
        """
        if session_id:
            user_session = self.user_id_by_session_id.get(session_id)
            if user_session:
                if self.session_duration <= 0:
                    return user_session.get('user_id')
                created_at = user_session.get('created_at')
                if created_at:
                    duration = timedelta(seconds=self.session_duration)
                    time = created_at + duration
                    if time > datetime.now():
                        return user_session.get('user_id')
        return None
