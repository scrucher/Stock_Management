from flask import *
from pony.orm import *
from ..Entity.Models import Supplier


class SupplierController:
    def create_supplier(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            Supplier(
                name=data['name'],
                location=data.get('location'),
                phone=data.get('phone'),
                email=data.get('email')
            )
            return jsonify({'message': 'Supplier created'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def delete_supplier(self, id):
        try:
            supplier = Supplier.get(id=id)
            if supplier:
                supplier.delete()
                return jsonify({'message': 'Supplier deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_supplier(self, id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            supplier = Supplier.get(id=id)
            if not supplier:
                return jsonify({'error': 'Supplier not found'}), 404
            supplier.set(
                name=data['name'],
                location=data.get('location'),
                phone=data.get('phone'),
                email=data.get('email')
            )
            return jsonify({'message': supplier.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_supplier(self):
        try:
            supplier = [s.to_dict() for s in Supplier.select()]
            if not supplier:
                return jsonify({'error': 'No supplier found'}), 404
            return jsonify({'list': supplier}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_supplier_by_id(self, id):
        try:
            supplier = Supplier.get(id=id)
            if not supplier:
                return jsonify({'error': 'Supplier not found'}), 404
            return jsonify({'list': supplier.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
