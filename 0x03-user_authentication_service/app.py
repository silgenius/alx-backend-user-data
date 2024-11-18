#!/usr/bin/env python3

"""
Route module for the API
"""

from flask import (
        Flask,
        jsonify,
        request,
        abort,
        make_response
        )
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def default():
    """
    return a JSON payload of the form:
    {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'])
def users():
    """
    The end-point should expect two form data fields: "email" and "password".
    If the user does not exist, the end-point should register it
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        new_user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"})
    else:
        return jsonify({"email": new_user.email, "message": "user created"})


@app.route('/sessions', methods=['POST'])
def login():
    """
     a login function to respond to the POST /sessions route
    """
    email = request.form.get('email')
    password = request.form.get('password')

    verify = AUTH.valid_login(email, password)
    if verify:
        new_session = AUTH.create_session(email)
        resp = make_response(jsonify(
            {
                "email": email,
                "message": "logged in"
            }
        ))
        resp.set_cookie("session_id", new_session)
        return resp
    raise abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
