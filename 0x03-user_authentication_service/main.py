#!/usr/bin/env python3

"""
query web server end point and check result validity
"""


import requests


def register_user(email: str, password: str) -> None:
    """
    test user registration
    """
    form_data = {'email': email, 'password': password}
    resp = requests.post('http://0.0.0.0:5000/users', data=form_data)

    assert resp.status_code == 200
    #print(resp.json())
    #assert resp.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    test log in with wrong password
    """
    form_data = {'email': email, 'password': password}
    resp = requests.post('http://0.0.0.0:5000/sessions', data=form_data)

    assert resp.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    test user log in
    """
    form_data = {'email': email, 'password': password}
    resp = requests.post('http://0.0.0.0:5000/sessions', data=form_data)

    assert resp.status_code != 401
    #print(resp.cookies.get('session_id'))
    return resp.cookies.get('session_id')


def profile_unlogged() -> None:
    """
    test profile not logged in
    """
    resp = requests.get('http://0.0.0.0:5000/profile')

    assert resp.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    test profile while logged n
    """
    cookie = {'session_id': str(session_id)}
    resp = requests.get('http://0.0.0.0:5000/profile', cookies=cookie)

    assert resp.status_code == 200


def log_out(session_id: str) -> None:
    """
    test user log out
    """
    cookie = {'session_id': session_id}
    resp = requests.delete('http://0.0.0.0:5000/sessions', cookies=cookie)

    #print(resp.status_code)
    assert resp.status_code == 200
    assert resp.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """
    test reset password
    """
    form_data = {'email': email}
    resp = requests.post('http://0.0.0.0:5000/reset_password', data=form_data)

    assert resp.status_code == 200
    #print(resp.json().get('reset_token'))
    return resp.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    test update password
    """
    form_data = {
            'email': email,
            'reset_token': reset_token,
            'new_password': new_password
            }
    resp = requests.put('http://0.0.0.0:5000/reset_password', data=form_data)

    assert resp.status_code == 200
    assert resp.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
