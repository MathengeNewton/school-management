from flask_login import UserMixin
from app.extensions import db, login_manager, bcrypt


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(UserMixin, db.Model):
    __tablename__ = 'admin_users'
    id = db.Column(db.String(100), primary_key=True, unique=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    status = db.Column(db.Integer)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def get_user_by_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
