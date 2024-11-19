#!/usr/bin/env python3

"""
Module -  for authentication
"""

import bcrypt
from db import DB, NoResultFound
import uuid
from typing import TypeVar, Union
from user import User


def _hash_password(password: str) -> bytes:
    """
    takes in a password string arguments and returns bytes.
    returned bytes is a salted hash of the input password,
    hashed with bcrypt.hashpw
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """
    return a string representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Initialize auth
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        take mandatory email and password string
        arguments and return a User object.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)

            user = self._db.add_user(
                    email=email,
                    hashed_password=hashed_password
                    )
            return user
        else:
            raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """
        locates the user by email. If it exists, check the password
        If it matches return True. In any other case, return False
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False

    def create_session(self, email: str) -> Union[str, None]:
        """
        takes an email string argument and returns
        the session ID as a string.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            self._db.update_user(user.id, session_id=_generate_uuid())
            return user.session_id

    def get_user_from_session_id(
            self,
            session_id: str = None
            ) -> Union[User, None]:
        """
        takes in session_id string argument and returns
        the corresponding User or None
        """
        if session_id:
            try:
                user = self._db.find_user_by(session_id=session_id)
            except NoResultFound:
                return None
            else:
                return user
        return None

    def destroy_session(self, user_id: str) -> str:
        """
        The method takes a single user_id integer argument and returns None
        The method updates the corresponding user’s session ID to None
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            pass
        else:
            self._db.update_user(user.id, session_id=None)
            return user.session_id

    def get_reset_password_token(self, email: str) -> str:
        """
         take an email string argument and returns a string.
         Finds the user corresponding to the email an
         generate a UUID and update the user’s reset_token
         database field
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        else:
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return user.reset_token
