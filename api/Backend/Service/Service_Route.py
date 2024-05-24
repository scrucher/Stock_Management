from flask import Blueprint
from .Service_Controller import ServiceController

service_bp = Blueprint('service', __name__)
service_controller = ServiceController()


@service_bp.route('/create', methods=['POST'])
def create():
    return service_controller.create_service()

@service_bp.route('/delete', methods=['DELETE'])
def delete():
    return service_controller.delete_services()

@service_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return service_controller.update_service(id)

@service_bp.route('/list', methods=['GET'])
def list_services():
    return service_controller.list_services()

@service_bp.route('/list/<int:id>', methods=['GET'])
def list_service_by_id(id):
    return service_controller.list_service_by_id(id)
