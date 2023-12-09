from flask import jsonify
from app import db

def get_all(model_class):
    all_items = model_class.query.all()
    result = [item.to_dict() for item in all_items]
    return result

def create(model_class, request_data):
    new_item = model_class(**request_data)
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

def get_one(model_class, item_id):
    item = model_class.query.get_or_404(item_id)
    return jsonify(item.to_dict())

def update(model_class, item_id, request_data):
    item = model_class.query.get_or_404(item_id)
    for key, value in request_data.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(item.to_dict())

def delete(model_class, item_id):
    item = model_class.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return '', 204
