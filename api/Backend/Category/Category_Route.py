from flask import Blueprint
from .Category_Controller import CategoryController

category_bp = Blueprint('category', __name__)
category_controller = CategoryController()


@category_bp.route('/create', methods=['POST'])
def create():
    return category_controller.create_category()

@category_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return category_controller.delete_category(id)

@category_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return category_controller.update_category(id)

@category_bp.route('/list', methods=['GET'])
def list_categorys():
    return category_controller.list_category()

@category_bp.route('/list/<int:id>', methods=['GET'])
def list_category_by_id(id):
    return category_controller.list_category_by_id(id)
