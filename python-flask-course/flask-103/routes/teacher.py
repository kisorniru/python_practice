from flask import Blueprint, jsonify, request, session
from models import db, Teacher
from routes.auth import admin_required

# Create a Blueprint for the student routes
teacher_bp = Blueprint("teacher", __name__)

@teacher_bp.route("/", methods=["GET"])
def index():
    # select * from teachers
    teachers = Teacher.query.all()
    
    # Clean, one-line list comprehension
    teachers_list = [teacher.to_dict() for teacher in teachers]

    response_data = {
        'message': 'List of all teachers',
        'teachers': teachers_list
    }
    
    return jsonify(response_data)

@teacher_bp.route("/", methods=["POST"])
@admin_required
def store():
    # create a new teacher record in the database
    name = request.form['name']
    email = request.form['email']

    teacher = Teacher(name=name, email=email, created_by=session['user_id'])

    db.session.add(teacher)
    try:
        db.session.commit()
        teacher_data = teacher.to_dict()
        response_data = {
            'message': 'Teacher created successfully',
            'teacher': teacher_data
        }
        return jsonify(response_data)
    except Exception as e:
        db.session.rollback()
        response_data = {
            'message': 'Error creating teacher',
            'error': str(e)
        }
        return jsonify(response_data), 500
    
@teacher_bp.route("/<int:id>", methods=["GET"])
def show(id):
    # select * from teachers where id = id
    teacher = Teacher.query.get(id)

    if teacher:
        response_data = {
            'message': 'Teacher found',
            'teacher': teacher.to_dict()
        }
        return jsonify(response_data)
    else:
        response_data = {
            'message': 'Teacher not found'
        }
        return jsonify(response_data), 404
    
@teacher_bp.route("/<int:id>", methods=["PUT"])
@admin_required
def update(id):
    # select * from teachers where id = id
    teacher = Teacher.query.get_or_404(id)

    # Update the teacher's name and email
    teacher.name = request.form['name']
    teacher.email = request.form['email']

    # why we don't db.session.add(teacher) here ?
    # Because the teacher object is already tracked by the SQLAlchemy session
    try:
        # 2. Check if another teacher is already using this new email
        existing_email = Teacher.query.filter(Teacher.email == teacher.email, Teacher.id != id).first()
        if existing_email:
            # Raising this immediately jumps execution to the 'except' block below
            raise ValueError(f'The email "{teacher.email}" is already taken by another teacher.')

        # 3. Save modifications
        db.session.commit()
        db.session.refresh(teacher)

        response_data = {
            'message': 'Teacher updated successfully',
            'teacher': teacher.to_dict()
        }
        return jsonify(response_data), 200
    except Exception as e:
        db.session.rollback()

        # 4. Extract the exact error message text from the exception instance
        response_data = {
            'message': 'Error updating teacher',
            'error': str(e)  # This captures your ValueError message or any unexpected DB crashes
        }
        
        # Proactively set a 400 Bad Request if it's our validation error, otherwise 500
        status_code = 400 if isinstance(e, ValueError) else 500
        return jsonify(response_data), status_code
    
@teacher_bp.route("/<int:id>", methods=["DELETE"])
@admin_required
def destroy(id):
    # select * from teachers where id = id
    teacher = Teacher.query.get_or_404(id)

    try:
        db.session.delete(teacher)
        db.session.commit()
        response_data = {
            'message': 'Teacher deleted successfully'
        }
        return jsonify(response_data), 200
    except Exception as e:
        db.session.rollback()
        response_data = {
            'message': 'Error deleting teacher',
            'error': str(e)
        }
        return jsonify(response_data), 500