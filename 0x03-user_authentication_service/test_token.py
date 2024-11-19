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
    reset_token = auth.get_reset_password_token(email)
except ValueError as err:
    print("could not create a new user: {}".format(err))
else:
    print(reset_token)

try:
    reset_token_2 = auth.get_reset_password_token("Does not exist")
except ValueError as err:
    print("could not create a new user: {}".format(err))
else:
    print(reset_token_2)

try:
    auth.update_password(reset_token, "newpwd")
except ValueError as err:
    print("Couldnt update password")
else:
    print(user.hashed_password)
    print(user.reset_token)

try:
    auth.update_password("wrong token", "new_pwd")
except ValueError as err:
    print("Couldnt update password")
else:
    print(user.hashed_password)
    print(user.reset_token)
