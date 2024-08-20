from flask import *
from .Product_Repository import ProductRepository
from ..Utilities.DTO import JSONResponse
from ..Utilities.Redis_Client import RedisClient


class ProductController:

    def __init__(self, product_repository: ProductRepository, redis_client: RedisClient):
        self.product_repository = product_repository
        self.redis_client = redis_client
        self.products = None
        self.product = None
        self.key = "Products"

    def create_product(self) -> JSONResponse:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data was Found'}), 404
        try:
            self.product = self.product_repository.add(data)
            data = self.product.to_dict()
            self.redis_client.set(self.key, data, self.product.id)
            return jsonify({'message': 'Product created'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def delete_product(self, product_id: int) -> JSONResponse:
        try:
            data = self.product_repository.get(product_id)
            if data:
                data.delete()
                self.redis_client.delete(self.key, product_id)
                return jsonify({'message': 'Product deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_product(self, product_id: int) -> JSONResponse:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data was found'}), 400
        try:
            product = self.product_repository.get(product_id)
            if not product:
                return jsonify({'error': 'Product not found'}), 404
            self.product = self.product_repository.update(product_id, data)
            data = self.product.to_dict()
            self.redis_client.set('Categories', data, self.product.id)
            return jsonify({'message': product.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_product(self) -> JSONResponse:
        product = self.redis_client.get_all(self.key)
        if not product:
            return jsonify({'error': 'No product found'}), 404
        return jsonify({'list': product}), 200

    def list_product_by_id(self, product_id: int) -> JSONResponse:
        self.products = self.redis_client.get_all(self.key)
        res = self.products[str(product_id)]
        if not self.products:
            return jsonify({'error': 'Product not found'}), 404
        return jsonify({'list': res}), 200
