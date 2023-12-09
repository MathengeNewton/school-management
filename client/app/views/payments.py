from flask   import render_template
from flask_login import login_required
from . import app
from ..models import Payments, SalesReps, Users
from ..utils.crudOperations import  *

@app.route('/payments', methods=['GET'])
@login_required
def allpayments():
    try:     
        payments = get_all(Payments)
        return render_template( 'home/payments.html', payments=payments )     
    except Exception as e:
        print(e)
        return render_template('home/page-500.html'), 500