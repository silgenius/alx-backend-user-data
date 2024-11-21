#!/usr/bin/env python3

"""
contains  a hash_password function that expects one string argument name
password and returns a salted, hashed password, which is a byte string.
"""

import bcrypt


def hash_password(password):
    """
    Uses the package to perform the hashing
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
