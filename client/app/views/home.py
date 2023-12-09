from flask   import render_template
from jinja2  import TemplateNotFound
from flask_login import login_required
from . import app
from app.utils.rabbitmq import publish 

@app.route('/', methods=['GET'])
@login_required
def index():
    try:     
        publish()
        return render_template( 'home/index.html' )    
    except:
        return render_template('home/page-500.html'), 500