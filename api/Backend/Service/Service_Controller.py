from flask import *
from .Service_Repository import ServiceRepository
from ..Utilities.DTO import JSONResponse
from ..Utilities.Redis_Client import RedisClient


class ServiceController:

    def __init__(self, service_repository: ServiceRepository, redis_client: RedisClient):
        self.service_repository = service_repository
        self.redis_client = redis_client
        self.services = None
        self.service = None
        self.key = "Categories"

    def create_service(self) -> JSONResponse:
        data = request.get_json()
        name: str = data.get('name')
        if not data:
            return jsonify({'error': 'No data was Found'}), 404
        try:
            self.service = self.service_repository.add(name)
            data = self.service.to_dict()
            self.redis_client.set(self.key, data, self.service.id)
            return jsonify({'message': 'Service created'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def delete_service(self, service_id: int) -> JSONResponse:
        try:
            data = self.service_repository.get(service_id)
            if data:
                data.delete()
                self.redis_client.delete(self.key, service_id)
                return jsonify({'message': 'Service deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_service(self, service_id: int) -> JSONResponse:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data was found'}), 400
        try:
            service = self.service_repository.get(service_id)
            if not service:
                return jsonify({'error': 'Service not found'}), 404
            self.service = self.service_repository.update(service_id, data.get('name'))
            data = self.service.to_dict()
            self.redis_client.set('Categories', data, self.service.id)
            return jsonify({'message': service.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_service(self) -> JSONResponse:
        service = self.redis_client.get_all(self.key)
        if not service:
            return jsonify({'error': 'No service found'}), 404
        return jsonify({'list': service}), 200

    def list_service_by_id(self, service_id: int) -> JSONResponse:
        self.services = self.redis_client.get_all(self.key)
        res = self.services[str(service_id)]
        if not self.services:
            return jsonify({'error': 'Service not found'}), 404
        return jsonify({'list': res}), 200
