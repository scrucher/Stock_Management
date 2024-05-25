from flask import Blueprint
from .Product_Controller import ProductController

product_bp = Blueprint('product', __name__)
product_controller = ProductController()


@product_bp.route('/create', methods=['POST'])
def create():
    return product_controller.create_product()

@product_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return product_controller.delete_product(id)

@product_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return product_controller.update_product(id)

@product_bp.route('/list', methods=['GET'])
def list_products():
    return product_controller.list_product()

@product_bp.route('/list/<int:id>', methods=['GET'])
def list_product_by_id(id):
    return product_controller.list_product_by_id(id)
