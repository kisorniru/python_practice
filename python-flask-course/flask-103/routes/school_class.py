from flask import Blueprint, jsonify, request, session
from models import db, SchoolClass
from routes.auth import admin_required

# Create a Blueprint for the class_teacher routes
school_class_bp = Blueprint("school_class", __name__)

@school_class_bp.route("/")
def index():
    school_classes = SchoolClass.query.all()
    school_classes_list = [school_class.to_dict() for school_class in school_classes]
    response_data = {
        'message': 'List of all school classes',
        'school_classes': school_classes_list
    }
    
    return jsonify(response_data), 200

@school_class_bp.route("/", methods=["POST"])
@admin_required
def store():
    # Validation Check
    # 1. Check if name feild exist
    if 'name' not in request.form:
        return jsonify({
            "message": "name feild is required"
        }), 400
    
    name = request.form['name']

    # 2. Check if name is empty
    if not name:
        return jsonify({
            "message": "Name cannot be empty"
        }), 400
    
    # 3. Check length
    if len(name) < 2:
        return jsonify({'message': 'Name must be at least 2 characters'}), 400
    if len(name) > 100:
        return jsonify({'message': 'Name cannot exceed 100 characters'}), 400
    
    # 4. Check for duplicates
    existing_class = SchoolClass.query.filter_by(name=name).first()
    if existing_class:
        return jsonify({
            "message": 'School class with this name already exists'
        }), 409

    new_school_class = SchoolClass(name=name, created_by=session['user_id'])
    
    db.session.add(new_school_class)
    try:
        db.session.commit()
        school_class_data = new_school_class.to_dict()
        response_data = {
            'message': 'School class created successfully',
            'school_class': school_class_data
        }
        return jsonify(response_data), 201
    except Exception as e:
        db.session.rollback()
        response_data = {
            'message': 'Error creating school class',
            'error': str(e)
        }
        return jsonify(response_data), 500
    
@school_class_bp.route("/<int:id>", methods=["PUT"])
@admin_required
def update(id):
    school_class = SchoolClass.query.get_or_404(id)
    name = request.form['name']
    school_class.name = name

    try:
        db.session.commit()
        # Refresh the instance to get the updated data
        db.session.refresh(school_class)
        response_data = {
            'message': 'School class updated successfully',
            'school_class': school_class.to_dict()
        }
        return jsonify(response_data), 200
    except Exception as e:
        db.session.rollback()
        response_data = {
            'message': 'Error updating school class',
            'error': str(e)
        }
        return jsonify(response_data), 500