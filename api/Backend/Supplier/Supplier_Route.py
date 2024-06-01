from flask import Blueprint
from .Supplier_Controller import SupplierController

supplier_bp = Blueprint('supplier', __name__)
supplier_controller = SupplierController()


@supplier_bp.route('/create', methods=['POST'])
def create():
    return supplier_controller.create_supplier()

@supplier_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return supplier_controller.delete_supplier(id)

@supplier_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return supplier_controller.update_supplier(id)

@supplier_bp.route('/list', methods=['GET'])
def list_suppliers():
    return supplier_controller.list_supplier()

@supplier_bp.route('/list/<int:id>', methods=['GET'])
def list_supplier_by_id(id):
    return supplier_controller.list_supplier_by_id(id)
