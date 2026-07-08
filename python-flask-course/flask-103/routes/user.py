from flask import Blueprint, jsonify, request
from models import db, User

# Create a Blueprint for the user routes
user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register():
    # Validation Check
    # 1. Check if username feild exist
    if username not in request.form:
        return jsonify({
            "message": "Username feild is required"
        }), 400
    
    # 1. Check if password feild exist
    if password not in request.form:
        return jsonify({
            "message": "Password feild is required"
        }), 400
    
    username = request.form['username']
    password = request.form['password']

    # 2. Check if username is empty
    if not username:
        return jsonify({
            "message": "Username cannot be empty"
        }), 400
    
    # 2. Check if password is empty
    if not password:
        return jsonify({
            "message": "password cannot be empty"
        }), 400
    
    # 3. Check length
    if len(username) < 3:
        return jsonify({'message': 'Username must be at least 3 characters'}), 400
    if len(username) > 100:
        return jsonify({'message': 'Username cannot exceed 100 characters'}), 400
    
    # 3. Check length
    if len(password) < 3:
        return jsonify({'message': 'Password must be at least 3 characters'}), 400
    if len(password) > 100:
        return jsonify({'message': 'Password cannot exceed 100 characters'}), 400
    
    # 4. Check for duplicates
    existing_username = User.query.filter_by(username=username).first()
    if existing_username:
        return jsonify({
            "message": 'Username name already exists'
        }), 409

    new_user = User(username=username, password=password)

    db.session.add(new_user)

    try:
        db.session.commit(new_user)
        new_user_data = new_user.to_dict()
        response_data = {
            'message': 'New user created successfully!',
            'new_user': new_user_data
        }
        return jsonify(response_data), 201
    except Exception as e:
        db.session.roolback()
        response_data = {
            'message': 'Error creating on user',
            'error': str(e)
        }
        return jsonify(response_data), 500
    
@user_bp.route("/login", methods=["POST"])
def login():
    # Validation Check
    # 1. Check if username feild exist
    if username not in request.form:
        return jsonify({
            "message": "Username feild is required"
        }), 400
    
    # 1. Check if password feild exist
    if password not in request.form:
        return jsonify({
            "message": "Password feild is required"
        }), 400
    
    username = request.form['username']
    password = request.form['password']

    # 2. Check if username is empty
    if not username:
        return jsonify({
            "message": "Username cannot be empty"
        }), 400
    
    # 2. Check if password is empty
    if not password:
        return jsonify({
            "message": "password cannot be empty"
        }), 400
    
    # 4. Check user existance
    user_exist = User.query.filter_by(username=username, password=password).first()
    if not user_exist:
        return jsonify({
            "message": 'Username not found'
        }), 404
    
    return jsonify({
        'message': 'user found'
    }), 200