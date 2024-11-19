#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'me@me.com'
password = 'mySecuredPwd'

auth = Auth()

try:
    user = auth.register_user(email, password)
    print("successfully created a new user!")
except ValueError as err:
    print("could not create a new user: {}".format(err))

try:
    user = auth.get_reset_password_token(email)
except ValueError as err:
    print("could not create a new user: {}".format(err))
else:
    print(user)

try:
    user = auth.get_reset_password_token("Does not exist")
except ValueError as err:
    print("could not create a new user: {}".format(err))
else:
    print(user)
