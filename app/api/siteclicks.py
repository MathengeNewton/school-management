from flask_restful import  Resource
from app import Clicks,db
from flask import request

class RegisterSiteClick(Resource):
    def post(self):
        """
        Register Click
        ---
        parameters:
          - in: body
            name: vendor
            description: Create Vendor
            required: true
            schema:
              type: object
              properties:
                ip_address:
                  type: string
                  description: Site visitor ip
                  example: 172.0.0.1
                location:
                  type: string
                  description: location
                  example: nairobi cbd
                client:
                  type: string
                  description: client 
                  example: ubuntu 22.04

        responses:
          200:
            description: Click registered successfully
            content:
              application/json:
                example: {"message": "Click registered successfully"}
        """
        try:
            # Parse JSON data from the request body
            data = request.get_json()

            # Validate and extract required fields
            ip_address = data['ip_address']
            location = data['location']
            client = data['client']

            # Create a new Vendor instance
            new_vendor = Clicks(ip_address=ip_address, location=location,client=client)
            # Set other fields on the new_vendor instance as needed

            # Add the new vendor to the database
            db.session.add(new_vendor)
            db.session.commit()

            return {'message': 'Click registered successfully'}
        except Exception as e:
            return {'message': f'Error: {str(e)}'}, 500