from database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    class_id = db.Column(db.Integer, db.ForeignKey('school_class.id'), nullable=False)

    # Relationship to SchoolClass
    school_class = db.relationship('SchoolClass')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "class_id": self.class_id,
            "class_name": self.school_class.name if self.school_class else None
        }