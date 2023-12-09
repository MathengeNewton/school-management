from flask_login import UserMixin
from app import db, Users
import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import relationship

class Categories(UserMixin, db.Model):
    __tablename__ = 'categories'
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, unique=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, server_default=func.now())
    updated_at = db.Column(db.Date)
    users = relationship('Users', backref='categories', cascade='all, delete-orphan',foreign_keys='Users.category_id')

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    @classmethod
    def get_category_by_id(cls, category_id):
        return cls.query.get(category_id)
    
    @classmethod
    def delete_category_and_user(cls, category_id):
        category = cls.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            
    @classmethod
    def count_users_per_category(cls):
        """
        Counts the number of users per category. Returns a list of tuples containing (category_id, category_name, user_count).
        """
        categories_with_user_count = db.session.query(
            Categories.id,
            Categories.name,
            func.count(Users.id)
        ).outerjoin(Users, Categories.users).group_by(Categories.id).all()

        return categories_with_user_count