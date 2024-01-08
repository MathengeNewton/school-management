from ..extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

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
    
class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    
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
        
class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    teacher = db.relationship('Teacher', backref='classes')
    
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
        
class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    school_class = db.relationship('Class', backref='sessions')
    
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
        
class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship('Student', backref='results')
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'))
    session = db.relationship('Session', backref='results')
    
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
        