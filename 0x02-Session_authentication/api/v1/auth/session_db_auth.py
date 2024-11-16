#!/usr/bin/env python3

"""
    Module - Auth
        A class to manage API authentication
"""

from .session_exp_auth import SessionExpAuth
import json
from datetime import datetime


TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S"


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
        self.load_from_file()

    def create_session(self, user_id=None):
        """
        creates a session id by calling create_session()
        and add to file
        """
        session_id = super().create_session(user_id)
        self.save_to_file()
        print(self.user_id_by_session_id)
        return session_id

    def destroy_session(self, request=None):
        """
        deletes the user session / logout
        """
        value = super().destroy_session(request)
        if value:
            self.save_to_file()
        return value

    def save_to_file(self):
        """
        save user_id_by_session_id to file
        """
        dup = self.user_id_by_session_id.copy()
        for v in dup.values():
            created_at = v.get('created_at')
            if created_at and type(created_at) is datetime:
                v['created_at'] = created_at.strftime(TIMESTAMP_FORMAT)
        with open(self.filename, 'w') as f:
            json.dump(dup, f)

    def load_from_file(self):
        """
        Load from file
        """
        try:
            with open(self.filename, 'r') as f:
                content = json.load(f)
        except FileNotFoundError:
            pass
        else:
            if content:
                for v in content.values():
                    created_at = v.get('created_at')
                    if created_at and isinstance(created_at, str):
                        v['created_at'] = datetime.strptime(
                                created_at,
                                TIMESTAMP_FORMAT
                                )
            self.user_id_by_session_id.update(content)
