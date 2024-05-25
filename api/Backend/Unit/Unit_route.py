from flask import Blueprint
from .Unit_controller import UnitController

unit_bp = Blueprint('unit', __name__)
unit_controller = UnitController()


@unit_bp.route('/create', methods=['POST'])
def create():
    return unit_controller.create_unit()

@unit_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return unit_controller.delete_unit(id)

@unit_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return unit_controller.update_unit(id)

@unit_bp.route('/list', methods=['GET'])
def list_units():
    return unit_controller.list_unit()

@unit_bp.route('/list/<int:id>', methods=['GET'])
def list_unit_by_id(id):
    return unit_controller.list_unit_by_id(id)
