from flask import Blueprint, jsonify, request
from models import db, SchoolClass

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
def store():
    name = request.form['name']
    
    new_school_class = SchoolClass(name=name)
    
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