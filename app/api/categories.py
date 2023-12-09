from flask_restful import Resource
from app import db  # Assuming Categories model is imported from app
from app.models import Categories
class GetCategories(Resource):
    def get(self):
        """
        Get all categories
        ---
        responses:
          200:
            description: Returns all categories
            content:
              application/json:
                example: {
                  "categories": [
                    {"id": "category_id_1", "name": "Category 1"},
                    {"id": "category_id_2", "name": "Category 2"},
                    ...
                  ]
                }
        """
        try:
            categories = Categories.query.all()
            categories_list = []
            for category in categories:
                categories_list.append({'id': str(category.id), 'name': category.name})

            return {'categories': categories_list}
        except Exception as e:
            return {'message': f'Error: {str(e)}'}, 500
