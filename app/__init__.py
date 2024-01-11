# -*- encoding: utf-8 -*-
import os
from datetime import datetime
from flask import Flask, request, redirect, url_for, render_template
from .models import Users, Subjects, Students, Classes,Results
from dotenv import load_dotenv
import os
from .extensions import (
    db,
    create_database,
    login_manager,
    bcrypt
)
from .config import Config
from flask_migrate import Migrate

# create app
app = Flask(__name__)
load_dotenv() 

current_directory = os.getcwd()
# Configure the SQLite database URI
# configure the Postgres database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nation.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
# initialize the app with the extension

def create_app():
    with app.app_context():
        create_database()

db.init_app(app)

# load Configuration
app.config.from_object(Config)
app.config['PER_PAGE'] = 25 

login_manager.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
    user = os.getenv('SUPER_ADMIN_USER')
    email = os.getenv('SUPER_ADMIN_USER_EMAIL')
    unhashedpass = os.getenv('SUPER_ADMIN_PASSWORD')

    # Check for the specific user
    specific_user = Users.query.filter_by(name=user).first()
    if specific_user is None:
        password = bcrypt.generate_password_hash(unhashedpass).decode('utf-8')
        created_at = datetime.now() 
        new_user = Users(name=user, email=email, password=password, is_admin=True,is_teacher=False, student_id="", is_parent=False, created_at = created_at)
        db.session.add(new_user)
        db.session.commit()
        
# Flask Login Management
@login_manager.user_loader
def load_user(user_id):
    # Replace this with your own logic to fetch the user object
    return Users.query.filter_by(id=user_id).first()

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@app.before_request
def redirect_unauthenticated():
    current_user = True    
    if not current_user and request.endpoint != "login":
        return redirect(url_for("login"))

# Import routing to render the pages
from app.views import *

@app.errorhandler(404)
def page_not_found(e):
    # Handle 404 errors here
    return render_template('home/page-404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    # Handle 404 errors here
    return render_template('home/page-500.html'), 500

@app.errorhandler(403)
def permissions_exception(e):
    # Handle 404 errors here
    return render_template('home/page-403.html'), 403