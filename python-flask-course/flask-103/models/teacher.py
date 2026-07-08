from database import db

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)

    # Relationship to ClassTeacher - one teacher has many classes
    classes = db.relationship("ClassTeacher", back_populates="teacher")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "classes": [ct.to_dict_of_class_for_teacher() for ct in self.classes]
        }