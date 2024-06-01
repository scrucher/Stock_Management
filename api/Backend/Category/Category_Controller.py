from flask import *
from pony.orm import *
from ..Entity.Models import Category


class CategoryController:
    def create_category(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            Category(
                name=data['name'],
            )
            return jsonify({'message': 'Category created'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def delete_category(self, id):
        try:
            category = Category.get(id=id)
            if category:
                category.delete()
                return jsonify({'message': 'Category deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_category(self, id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            category = Category.get(id=id)
            if not category:
                return jsonify({'error': 'Category not found'}), 404
            category.set(
                name=data['name'],
            )
            return jsonify({'message': category.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_category(self):
        try:
            category = [s.to_dict() for s in Category.select()]
            if not category:
                return jsonify({'error': 'No category found'}), 404
            return jsonify({'category': category}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_category_by_id(self, id):
        try:
            category = Category.get(id=id)
            if not category:
                return jsonify({'error': 'Category not found'}), 404
            return jsonify({'category': category.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
