#!/usr/bin/python3
""" Check response
"""
import requests
import base64
# from api.v1.auth.basic_auth import BasicAuth
from models.user import User


if __name__ == "__main__":

    """ Create a user test """
    user_email = "u3@hbtn.io"
    user_clear_pwd = "pwd"
    user = User()
    user.email = user_email
    user.password = user_clear_pwd
    print("New user: {} / {}".format(user.id, user.display_name()))
    user.save()

    basic_clear = "{}:{}".format(user_email, user_clear_pwd)
    r = requests.get('http://0.0.0.0:5000/api/v1/users', headers={ 'Authorization': "Basic {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")) })
    if r.status_code != 200:
        print("Wrong status code: {}".format(r.status_code))
        exit(1)
    if r.headers.get('content-type') != "application/json":
        print("Wrong content type: {}".format(r.headers.get('content-type')))
        exit(1)

    print("Well-deserved")
