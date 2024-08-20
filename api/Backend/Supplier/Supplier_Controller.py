from flask import *
from .Supplier_Repository import SupplierRepository
from ..Utilities.DTO import JSONResponse
from ..Utilities.Redis_Client import RedisClient


class SupplierController:

    def __init__(self, supplier_repository: SupplierRepository, redis_client: RedisClient):
        self.supplier_repository = supplier_repository
        self.redis_client = redis_client
        self.suppliers = None
        self.supplier = None
        self.key = "Suppliers"

    def create_supplier(self) -> JSONResponse:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data was Found'}), 404
        try:
            self.supplier = self.supplier_repository.add(data)
            data = self.supplier.to_dict()
            self.redis_client.set(self.key, data, self.supplier.id)
            return jsonify({'message': 'Supplier created'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def delete_supplier(self, supplier_id: int) -> JSONResponse:
        try:
            data = self.supplier_repository.get(supplier_id)
            if data:
                data.delete()
                self.redis_client.delete(self.key, supplier_id)
                return jsonify({'message': 'Supplier deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_supplier(self, supplier_id: int) -> JSONResponse:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data was found'}), 400
        try:
            supplier = self.supplier_repository.get(supplier_id)
            if not supplier:
                return jsonify({'error': 'Supplier not found'}), 404
            self.supplier = self.supplier_repository.update(supplier_id, data)
            data = self.supplier.to_dict()
            self.redis_client.set('Suppliers', data, self.supplier.id)
            return jsonify({'message': supplier.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_supplier(self) -> JSONResponse:
        supplier = self.redis_client.get_all(self.key)
        if not supplier:
            return jsonify({'error': 'No supplier found'}), 404
        return jsonify({'list': supplier}), 200

    def list_supplier_by_id(self, supplier_id: int) -> JSONResponse:
        self.suppliers = self.redis_client.get_all(self.key)
        res = self.suppliers[str(supplier_id)]
        if not self.suppliers:
            return jsonify({'error': 'Supplier not found'}), 404
        return jsonify({'list': res}), 200
