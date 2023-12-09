from flask   import render_template
from flask_login import login_required
from . import app
from ..models import Payments, SalesReps

@app.route('/sales-reps', methods=['GET'])
@login_required
def sales_reps():
    try:     
        return render_template( 'home/salesReps.html' )    
    except:
        return render_template('home/page-500.html'), 500