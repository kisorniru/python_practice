from flask import Blueprint

# Create a Blueprint for the class_teacher routes
class_teacher_bp = Blueprint("class_teacher", __name__)

@class_teacher_bp.route("/")
def class_teacher():
    return "This is the class teacher route."