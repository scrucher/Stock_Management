from flask import Blueprint, g
from .Service_Controller import ServiceController

service_bp = Blueprint('Service', __name__)


@service_bp.route('/create', methods=['POST'])
def create():
    return g.service_controller.create_service()

@service_bp.route('/delete', methods=['DELETE'])
def delete():
    return g.service_controller.delete_services()

@service_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return g.service_controller.update_service(id)

@service_bp.route('/list', methods=['GET'])
def list_services():
    return g.service_controller.list_services()

@service_bp.route('/list/<int:id>', methods=['GET'])
def list_service_by_id(id):
    return g.service_controller.list_service_by_id(id)
