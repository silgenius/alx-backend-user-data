#!/usr/bin/env python3

"""
Route module for the API
"""

from flask import (
        Flask,
        jsonify,
        request,
        abort,
        make_response,
        redirect,
        url_for
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


@app.route('/sessions', methods=['DELETE'])
def logout():
    """
    logout user
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect(url_for('default'))
    raise abort(403)


@app.route('/profile')
def profile():
    """
    function to respond to the GET /profile route.
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    raise abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """
     function to respond to the POST /reset_password route.
    """
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        raise abort(403)
    else:
        return jsonify({"email": email, "reset_token": reset_token}), 200


@app.route('/reset_password', methods=['PUT'])
def reset_password():
    """
     function in the app module to respond to
     the PUT /reset_password route.
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        raise abort(403)
    else:
        return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
