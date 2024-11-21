#!/usr/bin/env python3

"""
contains  a hash_password function that expects one string argument name
password and returns a salted, hashed password, which is a byte string.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Uses the package to perform the hashing
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Use bcrypt to validate that the provided
    password matches the hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
