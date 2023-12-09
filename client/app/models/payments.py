from flask_login import UserMixin
from app.extensions import db

class Payments(UserMixin, db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.String(100), primary_key=True, unique=True)
    TransactionType = db.Column(db.String(128))
    TransID = db.Column(db.String(64), index=True, unique=True)
    TransTime = db.Column(db.Date)
    TransAmount = db.Column(db.Integer)
    OrgAccountBalance = db.Column(db.Integer)
    ThirdPartyTransID = db.Column(db.String)
    MSISDN = db.Column(db.Integer)
    name = db.Column(db.String)
    created_at = db.Column(db.Date)
    
    def __repr__(self):
        return f"<Payments {self.id}>"
    
    @classmethod
    def sum_payments(cls):
        result = db.session.query(db.func.sum(cls.TransAmount)).scalar()
        return result or 0
