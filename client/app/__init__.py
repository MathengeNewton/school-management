# -*- encoding: utf-8 -*-
import os
# import Flask 
from flask import Flask, request, redirect, url_for, render_template
from .models import Users
from dotenv import load_dotenv
import os
from .extensions import (
    db,
    login_manager,
)
from .config import Config

# create app
app = Flask(__name__)
load_dotenv() 
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
# initialize the app with the extension
db.init_app(app)

# load Configuration
app.config.from_object(Config)

login_manager.init_app(app)

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

