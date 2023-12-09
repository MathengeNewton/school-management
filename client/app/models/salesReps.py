from flask_login import UserMixin
from app.extensions import db

class SalesReps(UserMixin, db.Model):
    __tablename__ = 'sales_reps'
    id = db.Column(db.String(100), primary_key=True, unique=True)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    phone = db.Column(db.String(128), unique=True)
    status = db.Column(db.Integer)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    
    def __repr__(self):
        return f"<Payments {self.id}>"
    
    @staticmethod
    def sum_by_status():
        result = db.session.query(db.func.sum(SalesReps.status)).filter(SalesReps.status == 1).scalar()
        return result or 0

