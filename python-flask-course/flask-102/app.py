from flask import Flask, request, redirect, flash, jsonify
from config import Config
from models import db, Student

# Flask app creating
app = Flask(__name__)
# Load the configuration from the Config class inside the application
app.config.from_object(Config)
# Initialize the database with the Flask app
db.init_app(app)

with app.app_context():
    # Create the database tables if they don't exist
    db.create_all()

# Get all students data
@app.route('/students', methods=['GET'])
def index_students():
    # select * from students
    students = Student.query.all()
    # TODO: Find a proper way for response
    # List a database object into a list of dictionaries
    students_list = []
    for student in students:
        students_list.append({
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'class_name': student.class_name,
            'admitted_at': student.admitted_at
        })

    response_data = {
        'message': 'List of all students',
        'students': students_list
    }
    
    return jsonify(response_data)

# Create a new student
@app.route('/students/create', methods=['GET'])
def create_student():
    return 'Creating a new student!'

# Store a new student
@app.route('/students/store', methods=['POST'])
def store_student():
    name = request.form['name']
    email = request.form['email']
    class_name = request.form['class_name']

    student = Student(name=name, email=email, class_name=class_name)
    db.session.add(student)
    try:
        db.session.commit()

        student_data = {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'class_name': student.class_name,
            'admitted_at': student.admitted_at
        }

        response_data = {
            'message': 'List of all students',
            'students': student_data
        }
        
        return jsonify(response_data)
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Show a student data
@app.route('/students/<int:id>', methods=['GET'])
def show_student(id):
    return f'Showing student with ID: {id}'

# Edits an existing student data
@app.route('/students/<int:id>/edit', methods=['GET'])
def edit_student(id):
    return f'Editing student with ID: {id}'

# Updates an existing student data
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)

    student.name = request.form['name']
    student.class_name = request.form['class_name']

    try:
        db.session.commit()

        student_data = {
            'id': student.id,
            'name': student.name,
            'email': student.email,
            'class_name': student.class_name,
            'admitted_at': student.admitted_at
        }

        response_data = {
            'message': 'Student updated successfully',
            'students': student_data
        }
        
        return jsonify(response_data)
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Deletes an existing student data
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)

    try:
        db.session.delete(student)
        db.session.commit()

        response_data = {
            'message': 'Student deleted successfully',
            'students': {
                'id': student.id,
                'name': student.name,
                'email': student.email,
                'class_name': student.class_name,
                'admitted_at': student.admitted_at
            }
        }
        
        return jsonify(response_data)
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

app.run(debug=True)