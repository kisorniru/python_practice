from database import db

class ClassTeacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('school_class.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    
    # Relationship to SchoolClass and Teacher
    school_class = db.relationship('SchoolClass')
    teacher = db.relationship('Teacher')

    # Relationship to ClassTeacher - one teacher has many classes
    teacher = db.relationship("Teacher", back_populates="classes")

    def to_dict(self):
        """Full details"""
        return {
            "id": self.id,
            "class_id": self.class_id,
            "class_name": self.school_class.name if self.school_class else None,
            "teacher_id": self.teacher_id,
            "teacher_name": self.teacher.name if self.teacher else None
        }
    
    def to_dict_of_class_for_teacher(self):
        """Used when returning from Teacher - excludes redundant teacher info"""
        return {
            "class_id": self.class_id,
            "class_name": self.school_class.name if self.school_class else None
        }