from flask import *
from .Category_Repository import CategoryRepository
from ..Utilities.DTO import JSONResponse
from ..Utilities.SearchAlgorithms import SearchAlgorithms


class CategoryController:

    def __init__(self, category_repository: CategoryRepository, search_algorithms: SearchAlgorithms, redis_client):
        self.category_repository = category_repository
        self.redis_client = redis_client
        self.categories = None
        self.category = None
        self.search_algorithms = search_algorithms
        self.key = 'Categories'

    def create_category(self) -> JSONResponse:
        data = request.get_json()
        name: str = data.get('name')
        if not data:
            return jsonify({'error': 'No data was Found'}), 404
        try:
            self.category = self.category_repository.add(name)
            data = {'id': self.category.id, 'name': self.category.name}
            self.redis_client.set(self.key, data, self.category.id)
            return jsonify({'message': 'Category created'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def delete_category(self, category_id: int) -> JSONResponse:
        try:

            if self.category_repository.get(category_id):
                self.category_repository.delete(category_id)
                self.redis_client.delete(self.key, category_id)
                return jsonify({'message': 'Category deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_category(self, category_id: int) -> JSONResponse:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data was found'}), 400
        try:
            category = self.category_repository.get(category_id)
            if not category:
                return jsonify({'error': 'Category not found'}), 404
            self.category = self.category_repository.update(category_id, data.get('name'))
            data = {'id': self.category.id, 'name': self.category.name}
            self.redis_client.set('Categories', data, self.category.id)
            return jsonify({'message': category.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_category(self) -> JSONResponse:
        category = self.redis_client.get_all(self.key)
        if not category:
            return jsonify({'error': 'No category found'}), 404
        return jsonify({'list': category}), 200

    def list_category_by_id(self, category_id: int) -> JSONResponse:
        self.categories = self.redis_client.get(self.key, category_id)
        if not self.category:
            return jsonify({'error': 'Category not found'}), 404
        return jsonify({'list': self.category.to_dict()}), 200
