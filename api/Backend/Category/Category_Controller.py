from flask import *
from .Category_Repository import CategoryRepository
from ..Utilities.DTO import JSONResponse
from ..Utilities import Redis_Client
from ..Utilities.ErrorHandling import ErrorHandling
import json


class CategoryController:

    def __init__(self, category_repository: CategoryRepository, redis_client: Redis_Client):
        self.category_repository = category_repository
        self.error_handling = ErrorHandling
        self.redis_client = redis_client
        self.categories = None
        self.category = None
        self.key = "Categories"

    def create_category(self) -> JSONResponse:
        data = request.get_json()
        name: str = data.get('name')
        if not data:
            return self.error_handling.not_found('Category')
        try:
            self.category = self.category_repository.add(name)
            data = self.category.to_dict()
            self.redis_client.set(self.key, data, self.category.id)
            return self.error_handling.success_created('Category')
        except Exception as e:
            return self.error_handling.forbidden()

    def delete_category(self, category_id: int) -> JSONResponse:
        try:
            data = self.category_repository.get(category_id)
            if data:
                data.delete()
                self.redis_client.delete(self.key, category_id)
                return self.error_handling.success_ok('Category Deletion Succeed')
        except Exception as e:
            return self.error_handling.internal_server_error()

    def update_category(self, category_id: int) -> JSONResponse:
        data = request.get_json()
        if not data:
            return self.error_handling.forbidden()
        try:
            category = self.category_repository.get(category_id)
            if not category:
                return self.error_handling.not_found('Category')
            self.category = self.category_repository.update(category_id, data.get('name'))
            data = self.category.to_dict()
            self.redis_client.set('Categories', data, self.category.id)
            return self.error_handling.success_ok('Category has been Updated Successfully')
        except Exception as e:
            return self.error_handling.internal_server_error()

    def list_category(self) -> JSONResponse:
        category = self.redis_client.get_all(self.key)
        if not category:
            return self.error_handling.not_found('No Category was')
        return self.error_handling.success_ok(category)

    def list_category_by_id(self, category_id: int) -> JSONResponse:
        self.categories = self.redis_client.get_all(self.key)
        res = self.categories[str(category_id)]
        if not res:
            return self.error_handling.not_found('Category')
        return self.error_handling.success_ok(res)
