from flask import *
from pony.orm import *
from ..Entity.Models import Service

class ServiceController:
    def create_service(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            Service(
                name=data['name'],
            )
            return jsonify({'message': 'Service created'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400


    def delete_service(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            service = Service.get(id=data['id'])
            if service:
                service.delete()
                return jsonify({'message': 'Service deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400