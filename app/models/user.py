from flask_login import UserMixin
from app.extensions import db, login_manager, bcrypt
import uuid
from sqlalchemy.dialects.postgresql import UUID


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
    student_id = db.Column(UUID(as_uuid=True), db.ForeignKey('students.id'), nullable = True)
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
    


from .classes import Classes
from .students import Students
Users.student = db.relationship('Students', backref='users')
Users.class_ = db.relationship('Classes', backref='users')        
    
    