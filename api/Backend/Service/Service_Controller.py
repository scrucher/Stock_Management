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

    def delete_services(self):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            service = Service.get(id=data['id'])
            if service:
                service.delete()
                return jsonify({'message': 'Service deleted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_service(self, id):
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        try:
            service = Service.get(id=id)
            if not service:
                return jsonify({'error': 'Service not found'}), 404
            service.set(
                name=data['name'],
            )
            return jsonify({'message': 'Service updated'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_services(self):
        try:
            services = [s.to_dict() for s in Service.select()]
            if not services:
                return jsonify({'error': 'No services found'}), 404
            return jsonify({'list': services}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def list_service_by_id(self, id):
        try:
            service = Service.get(id=id)
            if not service:
                return jsonify({'error': 'Service not found'}), 404
            return jsonify({'list': service.to_dict()}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
