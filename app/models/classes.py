from app.extensions import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Classes(db.Model):
    __tablename__ = 'classes'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    name = db.Column(db.String(64))
    class_code = db.Column(db.String(64), index=True, unique=True)
    class_teacher = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'))
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date, nullable=True)

    def __init__(self, name, class_code, class_teacher, created_at):
        self.name = name
        self.class_teacher = class_teacher
        self.class_code = class_code
        self.created_at = created_at

    @classmethod
    def get_class_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_class_by_class_code(cls, class_code):
        return cls.query.filter_by(class_code=class_code).first()
            
class Subjects():
    __tablename__ = 'subjects'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    name = db.Column(db.String(64), unique=True)
    pass_mark = db.Column(db.Integer)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date, nullable=True)
    
    def __init__(self, name, pass_mark,  created_at):
        self.name = name
        self.pass_mark = pass_mark
        self.created_at = created_at
        
    @classmethod
    def get_subject_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
