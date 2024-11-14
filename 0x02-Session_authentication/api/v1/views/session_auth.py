#!/usr/bin/env python3

"""
Module for session auth views
"""

from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models.user import User


@app_views.route(
        '/auth_session/login',
        methods=['POST'],
        strict_slashes=False
        )
def login_using_session():
    """
    Route: /auth_session/login
    Return: route for login
    """

    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    import os
    from api.v1.app import auth

    session_id = auth.create_session(user[0].id)

    resp = make_response(jsonify(user[0].to_json()))
    resp.set_cookie(os.getenv('SESSION_NAME'), session_id)

    return resp


@app_views.route(
        '/auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False
        )
def destroy_user_session():
    """
    Route: api/v1/views/session_auth.py
    Return:
        empty json dict
    """
    from api.v1.app import auth

    resp = auth.destroy_session(request)
    if resp:
        return jsonify({})
    raise abort(404)
