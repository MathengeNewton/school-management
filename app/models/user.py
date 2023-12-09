from flask_login import UserMixin
from app import db, login_manager, bcrypt, Categories
import uuid
from sqlalchemy.dialects.postgresql import UUID


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    status = db.Column(db.Boolean, default=False)
    category_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Categories.id'))
    is_admin = db.Column(db.Boolean)
    isActive = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date, nullable=True)
    
    def __init__(self, username, password, email, category_id, is_admin, created_at):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.category_id = category_id
        self.is_admin = is_admin

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
    def fetch_user_and_category(cls, email):
        return cls.query.join(Categories, cls.category_id == Categories.id).filter_by(email=email).first()
    
    