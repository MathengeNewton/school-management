from flask_restful import  Resource
from app import Customers,db
from flask import request

class RegisterCustomer(Resource):
    def post(self):
        """
        Register Customer
        ---
        parameters:
          - in: body
            name: customer
            description: Create customer
            required: true
            schema:
              type: object
              properties:
                fullname:
                  type: string
                  description: customer name
                  example: Example customer
                email:
                  type: string
                  description: customer email
                  example: customer@example.com
                phone:
                  type: string
                  description: Phone Number
                  example: +254700000000
                # Add other properties as needed

        responses:
          200:
            description: customer registered successfully
            content:
              application/json:
                example: {"message": "customer registered successfully"}
        """
        try:
            # Parse JSON data from the request body
            data = request.get_json()

            # Validate and extract required fields
            fullname = data['fullname']
            email = data['email']
            phone = data['phone']

            # Create a new customer instance
            new_customer = Customers(fullname=fullname, email=email,phone=phone)
            # Set other fields on the new_customer instance as needed

            # Add the new customer to the database
            db.session.add(new_customer)
            db.session.commit()

            return {'message': 'Customers registered successfully'}
        except Exception as e:
            return {'message': f'Error: {str(e)}'}, 500