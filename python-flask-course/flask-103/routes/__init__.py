from flask import Blueprint

from routes.main import main_bp
from routes.class_teacher import class_teacher_bp
from routes.school_class import school_class_bp
from routes.student import student_bp
from routes.teacher import teacher_bp
from routes.user import user_bp

def routes(app):
    # Create a master parent blueprint for version 1 of your API
    # And Register child blueprints onto the parent blueprint instead of 'app'
    api_v1_bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')

    # Register the main blueprint with the Flask api_v1_bp
    api_v1_bp.register_blueprint(user_bp, url_prefix="/user")

    # Register the main blueprint with the Flask api_v1_bp
    api_v1_bp.register_blueprint(main_bp, url_prefix="/")

    # Register the school_class blueprint with the Flask api_v1_bp
    api_v1_bp.register_blueprint(school_class_bp, url_prefix="/school-classes")

    # Register the class_teacher blueprint with the Flask api_v1_bp
    api_v1_bp.register_blueprint(class_teacher_bp, url_prefix="/class-teachers")
    
    # Register the student blueprint with the Flask api_v1_bp   
    api_v1_bp.register_blueprint(student_bp, url_prefix="/students")

    # Register the teacher blueprint with the Flask api_v1_bp
    api_v1_bp.register_blueprint(teacher_bp, url_prefix="/teachers")

    # Finally, register the single parent blueprint to the main app machine
    app.register_blueprint(api_v1_bp)