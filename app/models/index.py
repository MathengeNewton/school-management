from app.extensions import db, login_manager, bcrypt
import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))



class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean)
    is_teacher = db.Column(db.Boolean)
    is_parent = db.Column(db.Boolean)
    student_id = db.Column(db.String(64), nullable=True)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date, nullable=True)    
    
    def __init__(self, name, email,password,is_admin,is_teacher,is_parent, student_id, created_at):
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.is_teacher = is_teacher
        self.is_parent = is_parent
        self.student_id = student_id
        self.created_at = created_at

    def get_user_by_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def get_user_by_student_id(cls, student_id):
        return cls.query.filter_by(student_id=student_id).all()
    
class Classes(db.Model):
    __tablename__ = 'classes'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    name = db.Column(db.String(64))
    class_code = db.Column(db.String(64), index=True, unique=True)
    class_teacher = db.Column(db.String(64), nullable=True)
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
    
    
    

class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    name = db.Column(db.String(64))
    class_ = db.Column(db.String(64), index=True, unique=True)
    parent_id = db.Column(db.String(64),nullable=True)
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
    student_id = db.Column(db.String(64),nullable=True)
    subject_id = db.Column(db.String(64),nullable=True)
    entered_by = db.Column(db.String(64),nullable=True)
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
