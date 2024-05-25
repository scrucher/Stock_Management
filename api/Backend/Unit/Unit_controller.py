from flask import *
from pony.orm import *
from ..Entity.Models import Unit


class UnitController:
    def create_unit(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            Unit(
                name=data['name'],
            )
            return jsonify({'message': 'Unit created'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def delete_unit(self, id):
        try:
            unit = Unit.get(id=id)
            if unit:
                unit.delete()
                return jsonify({'message': 'Unit deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_unit(self, id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            unit = Unit.get(id=id)
            if not unit:
                return jsonify({'error': 'Unit not found'}), 404
            unit.set(
                name=data['name'],
            )
            return jsonify({'message': unit.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_unit(self):
        try:
            unit = [s.to_dict() for s in Unit.select()]
            if not unit:
                return jsonify({'error': 'No unit found'}), 404
            return jsonify({'unit': unit}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_unit_by_id(self, id):
        try:
            unit = Unit.get(id=id)
            if not unit:
                return jsonify({'error': 'Unit not found'}), 404
            return jsonify({'unit': unit.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
