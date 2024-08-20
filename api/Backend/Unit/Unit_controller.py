from flask import *
from .Unit_Repository import UnitRepository
from ..Utilities.DTO import JSONResponse
from ..Utilities.Redis_Client import RedisClient


class UnitController:

    def __init__(self, unit_repository: UnitRepository, redis_client: RedisClient):
        self.unit_repository = unit_repository
        self.redis_client = redis_client
        self.units = None
        self.unit = None
        self.key = "Units"

    def create_unit(self) -> JSONResponse:
        data = request.get_json()
        name: str = data.get('name')
        if not data:
            return jsonify({'error': 'No data was Found'}), 404
        try:
            self.unit = self.unit_repository.add(name)
            data = self.unit.to_dict()
            self.redis_client.set(self.key, data, self.unit.id)
            return jsonify({'message': 'Unit created'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def delete_unit(self, unit_id: int) -> JSONResponse:
        try:
            data = self.unit_repository.get(unit_id)
            if data:
                data.delete()
                self.redis_client.delete(self.key, unit_id)
                return jsonify({'message': 'Unit deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_unit(self, unit_id: int) -> JSONResponse:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data was found'}), 400
        try:
            unit = self.unit_repository.get(unit_id)
            if not unit:
                return jsonify({'error': 'Unit not found'}), 404
            self.unit = self.unit_repository.update(unit_id, data.get('name'))
            data = self.unit.to_dict()
            self.redis_client.set('Categories', data, self.unit.id)
            return jsonify({'message': unit.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_unit(self) -> JSONResponse:
        unit = self.redis_client.get_all(self.key)
        if not unit:
            return jsonify({'error': 'No unit found'}), 404
        return jsonify({'list': unit}), 200

    def list_unit_by_id(self, unit_id: int) -> JSONResponse:
        self.units = self.redis_client.get_all(self.key)
        res = self.units[str(unit_id)]
        if not self.units:
            return jsonify({'error': 'Unit not found'}), 404
        return jsonify({'list': res}), 200
