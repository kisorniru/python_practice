from flask import Blueprint, jsonify, request
from models import db, ClassTeacher

# Create a Blueprint for the class_teacher routes
class_teacher_bp = Blueprint("class_teacher", __name__)

@class_teacher_bp.route("/", methods=["GET"])
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

@class_teacher_bp.route("/", methods=["POST"])
def store():
    # Get the JSON data from the request
    data = request.get_json()
    class_id = data["class_id"]
    teacher_id = data["teacher_id"]

    # Create a new ClassTeacher
    new_class_teacher = ClassTeacher(class_id=class_id, teacher_id=teacher_id)

    db.session.add(new_class_teacher)
    try:
        db.session.commit()
        class_teacher_data = new_class_teacher.to_dict()
        response_data = {
            "message": "Class teacher assigned successfully!",
            "class_teacher": class_teacher_data
        }
        return jsonify(response_data), 201
    except Exception as e:
        db.session.roolback()
        response_data = {
            "message": "Error on creating class teacher",
            "error": str(e)
        }
        return jsonify(response_data), 500
