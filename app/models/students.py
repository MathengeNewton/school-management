import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.extensions import db

class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    name = db.Column(db.String(64))
    class_ = db.Column(db.String(64), index=True, unique=True)
    parent_id = db.Column(UUID(as_uuid=True))
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date, nullable=True)
    
    def __init__(self, name, class_, parent_id, created_at):
        self.name = name
        self.parent_id = parent_id
        self.class_ = class_
        self.created_at = created_at

    def get_user_by_id(self):
        return str(self.id)

    @classmethod
    def get_parent_details(cls, email):
        return cls.query.filter_by(email=email).first()
    
class Results(db.Model):
    __tablename__ = 'results'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    student_id = db.Column(UUID(as_uuid=True), db.ForeignKey('students.id'), nullable=False)
    subject_id = db.Column(UUID(as_uuid=True), db.ForeignKey('subjects.id'), nullable=False)
    entered_by = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
    marks = db.Column(db.Integer)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date, nullable=True)
    
    def __init__(self, student_id, subject_id, entered_by, marks, created_at):
        self.student_id = student_id
        self.subject_id = subject_id
        self.entered_by = entered_by
        self.marks = marks
        self.created_at = created_at

    def get_result_by_id(self):
        return str(self.id)

    @classmethod
    def get_result_by_student(cls, student_id):
        return cls.query.filter_by(student_id=student_id).all()
    
    @classmethod
    def get_result_by_student_and_subject(cls, student_id,subject_id):
        return ( cls.query
                    .filter_by(student_id=student_id)
                    .filter_by(subject_id=subject_id)
                    .all()
            )



from .user import Users
parent = db.relationship('Users', backref='students')