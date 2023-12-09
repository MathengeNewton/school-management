from flask_restful import  Resource
from app import Vendors,db, Emails
from flask import request

class RegisterVendor(Resource):
    def post(self):
        """
        Register vendor
        ---
        parameters:
          - in: body
            name: vendor
            description: Create Vendor
            required: true
            schema:
              type: object
              properties:
                business_name:
                  type: string
                  description: Business name
                  example: Example Vendor
                  required: true
                contact_person:
                  type: string
                  description: Contact Person
                  example: John Doe
                  required: true
                contact_person_email:
                  type: string
                  description: Contact person's email
                  example: mail@mail.com
                  required: true
                contact_person_phone:
                  type: string
                  description: Contact Person's Phone number
                  example: +245788890989
                  required: true
                category_id:
                  type: string
                  description: category id
                  example: u34uish-wenii39f-34fvv34
                  required: true
                business_website:
                  type: string
                  description: Business Website if any
                  example: https://website.co
                  required: false                
                # Add other properties as needed

        responses:
          200:
            description: Vendor registered successfully
            content:
              application/json:
                example: {"message": "Vendor registered successfully"}
        """
        try:
            # Parse JSON data from the request body
            data = request.get_json()

            # Validate and extract required fields
            business_name = data['business_name']
            contact_person = data['contact_person']
            contact_person_email = data['contact_person_email']
            contact_person_phone = data['contact_person_phone']
            category_id = data['category_id']
            business_website = data['business_website']
            
            new_vendor = Vendors(
                            business_name=business_name, 
                            contact_person=contact_person, 
                            contact_person_email=contact_person_email, 
                            contact_person_phone=contact_person_phone, 
                            category_id=category_id,
                            business_website=business_website
                          )
            
            
            # Add the new vendor to the database
            db.session.add(new_vendor)
            db.session.commit()
            
            new_mail = Emails(
                            email=contact_person_email, 
                            vendor=business_name
                          )            
            db.session.add(new_mail)
            db.session.commit()

            return {'message': 'Vendor registered successfully'}
        except Exception as e:
            return {'message': f'Error: {str(e)}'}, 500