from database import db

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)

    def to_dict(self):
        # Dynamically converts all columns into a dictionary
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}