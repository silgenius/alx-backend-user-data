#!/usr/bin/env python3

""" UserSession module
"""

import hashlib
from models.base import Base


class UserSession(Base):
    """
    UserSesson
    """
    def __init__(self, *args: list, **kwargs: dict):
        """
        Initialize user session
        """
        super().__init__(*args, **kwargs)
        if args:
            self.user_id = args[0]
            self.session_id = args[1]

        if kwargs and kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)
