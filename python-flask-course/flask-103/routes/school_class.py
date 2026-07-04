from flask import Blueprint

# Create a Blueprint for the class_teacher routes
school_class_bp = Blueprint("school_class", __name__)

@school_class_bp.route("/")
def school_class():
    return "This is the school class route."