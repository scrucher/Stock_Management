from flask import Blueprint,g

supplier_bp = Blueprint('Supplier', __name__)


@supplier_bp.route('/create', methods=['POST'])
def create():
    return g.supplier_controller.create_supplier()

@supplier_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return g.supplier_controller.delete_supplier(id)

@supplier_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return g.supplier_controller.update_supplier(id)

@supplier_bp.route('/list', methods=['GET'])
def list_suppliers():
    return g.supplier_controller.list_supplier()

@supplier_bp.route('/list/<int:id>', methods=['GET'])
def list_supplier_by_id(id):
    return g.supplier_controller.list_supplier_by_id(id)
