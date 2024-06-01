from flask import *
from pony.orm import *
from ..Entity.Models import Stock


class StockController:
    def create_stock(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:


            Stock(
                product=data['product_id'],
                stock_security=data['stock_security'],
                stock_max=data['stock_max'],
                unit_price=data['unit_price'],
                current_stock=data['current_stock']
                )
            return jsonify({'message': 'Stock created'}), 201

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete_stock(self, id):
        try:
            stock = Stock.get(id=id)
            if stock:
                stock.delete()
                return jsonify({'message': 'Stock deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_stock(self, id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            stock = Stock.get(id=id)
            if not stock:
                return jsonify({'error': 'Stock not found'}), 404
            stock.set(
                product_id=data['product_id'],
                stock_security=data['stock_security'],
                stock_max=data['stock_max'],
                unit_price=data['unit_price'],
                current_stock=data['current_stock']
            )
            return jsonify({'message': stock.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_stock(self):
        try:
            stock = [s.to_dict() for s in Stock.select()]
            if not stock:
                return jsonify({'error': 'No stock found'}), 404
            return jsonify({'stock': stock}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_stock_by_id(self, id):
        try:
            stock = Stock.get(id=id)
            if not stock:
                return jsonify({'error': 'Stock not found'}), 404
            return jsonify({'stock': stock.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
