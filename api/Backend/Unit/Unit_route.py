from flask import Blueprint,g
from .Unit_controller import UnitController

unit_bp = Blueprint('unit', __name__)


@unit_bp.route('/create', methods=['POST'])
def create():
    return g.unit_controller.create_unit()

@unit_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return g.unit_controller.delete_unit(id)

@unit_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return g.unit_controller.update_unit(id)

@unit_bp.route('/list', methods=['GET'])
def list_units():
    return g.unit_controller.list_unit()

@unit_bp.route('/list/<int:id>', methods=['GET'])
def list_unit_by_id(id):
    return g.unit_controller.list_unit_by_id(id)
