from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), nullable=True, unique=True)
    class_name = db.Column(db.String(60), nullable=True)
    admitted_at = db.Column(db.DateTime, default=datetime.now())