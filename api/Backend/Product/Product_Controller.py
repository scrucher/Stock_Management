from flask import *
from pony.orm import *
from ..Entity.Models import Product


class ProductController:
    def create_product(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            Product(
                name=data['name'],
                image_name=data['image_name'],
                category=data['category'],
                expiration_date=data['expiration_date'],
                unit_price=data['unit_price'],
                unit=data['unit']
            )
            return jsonify({'message': 'Product created'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def delete_product(self, id):
        try:
            product = Product.get(id=id)
            if product:
                product.delete()
                return jsonify({'message': 'Product deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_product(self, id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            product = Product.get(id=id)
            if not product:
                return jsonify({'error': 'Product not found'}), 404
            product.set(
                name=data['name'],
                image_name=data['image_name'],
                category=data['category_id'],
                expiration_date=data['expiration_date'],
                unit_price=data['unit_price'],
                unit_id=data['unit_id']
            )
            return jsonify({'message': product.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_product(self):
        try:
            product = [s.to_dict() for s in Product.select()]
            if not product:
                return jsonify({'error': 'No product found'}), 404
            return jsonify({'product': product}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_product_by_id(self, id):
        try:
            product = Product.get(id=id)
            if not product:
                return jsonify({'error': 'Product not found'}), 404
            return jsonify({'product': product.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
