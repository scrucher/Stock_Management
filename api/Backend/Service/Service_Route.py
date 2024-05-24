from flask import Blueprint
from .Service_Controller import ServiceController

service_bp = Blueprint('service', __name__)
service_controller = ServiceController()


@service_bp.route('/create', methods=['POST'])
def create():
    return service_controller.create_service()
