from database import db

class ClassTeacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('school_class.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "class_id": self.class_id,
            "teacher_id": self.teacher_id
        }