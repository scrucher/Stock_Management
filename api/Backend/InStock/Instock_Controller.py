from flask import *
from pony.orm import *
from ..Entity.Models import InboundStock, Stock
from ..Stock.Stock_Controller import StockController


class InboundStockController:
    def create_in_stock(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        required_fields = ['quantity', 'product', 'supplier', 'unit_price', 'user', 'tva_rate', 'invoice', 'exp_date']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'{field} is required'}), 400

        try:
            with db_session:
                in_stock = InboundStock(
                    quantity=data['quantity'],
                    product=data['product'],
                    supplier=data['supplier'],
                    unit_price=data['unit_price'],
                    user=data['user'],
                    tva_rate=data['tva_rate'],
                    invoice=data['invoice'],
                )

                if in_stock:
                    stock_query = select(
                        s for s in Stock if s.product == data['product'] and s.exp_date == data['exp_date'])
                    stock = stock_query.first()  # Execute the query to get the first matching stock

                    if stock:
                        stock.quantity += data['quantity']
                    else:
                        StockController.create_stock(data)

                    return jsonify({'message': 'Data Inserted Successfully'}), 201

        except KeyError as e:
            return jsonify({'error': f'Missing field in data: {str(e)}'}), 400
        except Exception as e:
            return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

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
