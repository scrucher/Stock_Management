from flask import *
from pony.orm import *
from ..Entity.Models import OutboundStock, Stock


class OutboundStockController:
    def create_out_stock(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        required_fields = ['quantity', 'product', 'supplier', 'unit_price', 'user', 'tva_rate', 'invoice', 'exp_date']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'{field} is required'}), 400

        try:
            with db_session:
                out_stock = OutboundStock(
                    quantity=data['quantity'],
                    product=data['product'],
                    supplier=data['supplier'],
                    unit_price=data['unit_price'],
                    user=data['user'],
                    tva_rate=data['tva_rate'],
                    invoice=data['invoice'],
                )

                if out_stock:
                    stock_query = select(s for s in Stock if s.product == data['product'] and s.exp_date == data['exp_date'])
                    stock = stock_query.first()  # Execute the query to get the first matching stock

                    if stock:
                        stock.quantity -= data['quantity']
                    else:
                        return jsonify({'error': 'No Data Was Found '}), 201

                    return jsonify({'message': 'Data Inserted Successfully'}), 201

        except KeyError as e:
            return jsonify({'error': f'Missing field in data: {str(e)}'}), 400
        except Exception as e:
            return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

    def delete_out_stock(self, id):
        try:
            out_stock = OutboundStock.get(id=id)
            if out_stock:
                out_stock.delete()
                return jsonify({'message': 'OutboundStock deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_out_stock(self, id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            out_stock = OutboundStock.get(id=id)
            if not out_stock:
                return jsonify({'error': 'OutboundStock not found'}), 404
            out_stock.set(
                quantity=data['quantity'],
                product_id=data['product_id'],
                supplier_id=data['supplier_id'],
                unit_price=data['unit_price'],
                user_id=data['user_id'],
                tva_rate=data['tva_rate'],
                invoice=data['invoice']
            )
            return jsonify({'message': out_stock.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_out_stock(self):
        try:
            out_stock = [s.to_dict() for s in OutboundStock.select()]
            if not out_stock:
                return jsonify({'error': 'No out_stock found'}), 404
            return jsonify({'out_stock': out_stock}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

