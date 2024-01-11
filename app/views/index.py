from flask   import render_template,  flash, redirect, url_for
from jinja2  import TemplateNotFound
from flask_login import  logout_user,  login_required
from app import app

@app.route('/home', methods=['GET','POST'])
def index():
    try:                       
        return render_template('admin/home/index.html')    
    except Exception as e:        
        flash('Invalid username or password')
        return render_template('home/sign-in.html')
    
@app.route('/logout')
# @login_required
def logout():
    # logout_user()  # clear the user session
    resp = redirect(url_for('index'))
    resp.set_cookie('session', '', max_age=0)  # force the session cookie to expire
    return resp

@app.route('/reset-password', methods=['GET'])
def resetpassword():
    try:        
        return render_template( 'home/reset-password.html' )    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404