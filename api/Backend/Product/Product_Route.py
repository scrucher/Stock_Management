from flask import Blueprint,g

product_bp = Blueprint('Product', __name__)


@product_bp.route('/create', methods=['POST'])
def create():
    return g.product_controller.create_product()

@product_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return g.product_controller.delete_product(id)

@product_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return g.product_controller.update_product(id)

@product_bp.route('/list', methods=['GET'])
def list_products():
    return g.product_controller.list_product()

@product_bp.route('/list/<int:id>', methods=['GET'])
def list_product_by_id(id):
    return g.product_controller.list_product_by_id(id)
