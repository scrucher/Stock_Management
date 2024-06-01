from flask import *
from pony.orm import *
from ..Entity.Models import InboundStock


class InboundStockController:
    def create_in_stock(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            InboundStock(
                    quantity=data['quantity'],
                    product=data['product'],
                    supplier=data['supplier'],
                    unit_price=data['unit_price'],
                    user=data['user'],
                    tva_rate=data['tva_rate'],
                    invoice=data['invoice'],
                )
            return jsonify({'message': 'InboundStock created'}), 201

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete_in_stock(self, id):
        try:
            in_stock = InboundStock.get(id=id)
            if in_stock:
                in_stock.delete()
                return jsonify({'message': 'InboundStock deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_in_stock(self, id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            in_stock = InboundStock.get(id=id)
            if not in_stock:
                return jsonify({'error': 'InboundStock not found'}), 404
            in_stock.set(
                quantity=data['quantity'],
                product_id=data['product_id'],
                supplier_id=data['supplier_id'],
                unit_price=data['unit_price'],
                user_id=data['user_id'],
                tva_rate=data['tva_rate'],
                invoice=data['invoice']
            )
            return jsonify({'message': in_stock.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_in_stock(self):
        try:
            in_stock = [s.to_dict() for s in InboundStock.select()]
            if not in_stock:
                return jsonify({'error': 'No in_stock found'}), 404
            return jsonify({'in_stock': in_stock}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_in_stock_by_id(self, id):
        try:
            in_stock = InboundStock.get(id=id)
            if not in_stock:
                return jsonify({'error': 'InboundStock not found'}), 404
            return jsonify({'in_stock': in_stock.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
