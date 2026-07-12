from functools import wraps
from flask import jsonify, session
from models import db, User


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({
                "message": "Please login!"
            }), 401

        user = User.query.get(session['user_id'])
        if not user:
            return jsonify({
                "message": "Please login!"
            }), 401

        return f(*args, **kwargs)

    return decorated_function


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({
                "message": "Please login!"
            }), 401

        user = User.query.get(session['user_id'])
        if not user:
            return jsonify({
                "message": "Please login!"
            }), 401

        if user.usertype != 'admin':
            return jsonify({
                "message": "You are not authorized to perform this action."
            }), 403

        return f(*args, **kwargs)

    return decorated_function
