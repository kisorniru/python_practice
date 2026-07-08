from flask import Blueprint, jsonify, request, session
from models import db, Student, SchoolClass
from routes.auth import login_required, admin_required

# Create a Blueprint for the student routes
student_bp = Blueprint("student", __name__)

@student_bp.route("/")
def index():
    students = Student.query.all()
    students_list = [student.to_dict() for student in students]
    response_data = {
        'message': 'List of all students',
        'students': students_list
    }
    
    return jsonify(response_data), 200

@student_bp.route("/", methods=["POST"])
@login_required
def store():
    name = request.form['name']
    email = request.form['email']
    class_id = request.form['class_id']

    new_student = Student(name=name, email=email, class_id=class_id, created_by=session['user_id'])
    db.session.add(new_student)

    try:
        class_exists = SchoolClass.query.get(class_id) is not None

        if not class_exists:
            raise ValueError(f"Class with ID {class_id} does not exist.")

        db.session.commit()
        student_data = new_student.to_dict()
        response_data = {
            'message': 'Student created successfully',
            'student': student_data
        }
        return jsonify(response_data), 201
    except Exception as e:
        db.session.rollback()
        response_data = {
            'message': 'Error creating student',
            'error': str(e)
        }
        return jsonify(response_data), 500
    
@student_bp.route("/<int:id>", methods=["GET"])
def show(id):
    student = Student.query.get_or_404(id)

    if student:
        response_data = {
            'message': 'Student found',
            'student': student.to_dict()
        }
        return jsonify(response_data), 200
    else:
        response_data = {
            'message': 'Student not found'
        }
        return jsonify(response_data), 404
    
@student_bp.route("/<int:id>", methods=["PUT"])
@admin_required
def update(id):
    student = Student.query.get_or_404(id)

    student.name = request.form['name']
    student.email = request.form['email']
    student.class_id = request.form['class_id']

    try:
        class_exists = SchoolClass.query.get(student.class_id) is not None

        if not class_exists:
            raise ValueError(f"Class with ID {student.class_id} does not exist.")

        db.session.commit()
        response_data = {
            'message': 'Student updated successfully',
            'student': student.to_dict()
        }
        return jsonify(response_data), 200
    except Exception as e:
        db.session.rollback()
        response_data = {
            'message': 'Error updating student',
            'error': str(e)
        }
        return jsonify(response_data), 500