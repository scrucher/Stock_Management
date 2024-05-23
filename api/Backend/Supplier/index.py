from ..Entity.Models import Supplier
from pony.orm import *
from flask import *


class supplier:
    def __init__(self):
        self.supplier = Supplier()

    def create_supplier(self):
        try:
            supp = self.supplier.get(id=request.json['id'])
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        if supp:
            return jsonify({'err': 'Supplier already exists'}), 200
        else:
            try:
                self.supplier.name = request.json['name']
                commit()
                return jsonify({'err': 'Supplier created'}), 201
            except Exception as e:
                return jsonify({'err': str(e)}), 500

    def update_supplier(self):
        try:
            supp = self.supplier.get(id=request.json['id'])
            if not supp:
                return jsonify({'err': 'Supplier not found'}), 404
            supp.name = request.json['name']
            commit()
            return jsonify({'msg': 'Supplier updated'}), 200
        except Exception as e:
            return jsonify({'err': str(e)}), 500

    def get_supplier(self):
        try:
            supp = self.supplier.get(id=request.json['id'])
            if supp:
                return jsonify({'msg': supp}), 404
            else:
                return jsonify({'err': 'Supplier not found'}), 404
        except Exception as e:
            return jsonify({'err': str(e)}), 500

    def get_supplier_list(self):
        try:
            supp = self.supplier.select().order_by(desc(Supplier.id))
            if supp:
                return jsonify({'msg': supp}), 200
            else:
                return jsonify({'err': 'Suppliers not found'}), 404
        except Exception as e:
            return jsonify({'err': str(e)}), 500
