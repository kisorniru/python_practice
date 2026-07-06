from flask import Blueprint, jsonify
from models import db, ClassTeacher

# Create a Blueprint for the class_teacher routes
class_teacher_bp = Blueprint("class_teacher", __name__)

@class_teacher_bp.route("/")
def index():
    # Query all ClassTeacher records from the database
    class_teachers = ClassTeacher.query.all()

    # Convert the records to a list of dictionaries
    class_teachers_list = [class_teacher.to_dict() for  class_teacher in class_teachers]

    response_data = {
        'message': 'List of all class teachers',
        'class_teachers': class_teachers_list
    }

    return jsonify(response_data), 200