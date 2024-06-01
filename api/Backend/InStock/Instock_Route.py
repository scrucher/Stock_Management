from flask import Blueprint
from .Instock_Controller import InboundStockController

in_stock_bp = Blueprint('in_stock', __name__)
in_stock_controller = InboundStockController()


@in_stock_bp.route('/create', methods=['POST'])
def create():
    return in_stock_controller.create_in_stock()


@in_stock_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    return in_stock_controller.delete_in_stock(id)


@in_stock_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    return in_stock_controller.update_in_stock(id)


@in_stock_bp.route('/list', methods=['GET'])
def list_in_stocks():
    return in_stock_controller.list_in_stock()


@in_stock_bp.route('/list/<int:id>', methods=['GET'])
def list_in_stock_by_id(id):
    return in_stock_controller.list_in_stock_by_id(id)
