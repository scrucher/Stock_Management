from flask import Blueprint, g, jsonify

category_bp = Blueprint('Category', __name__)


@category_bp.before_app_request
def load_controller():
    g.category_controller = g.get('category_controller', None)


@category_bp.route('/create', methods=['POST'])
def create():
    if g.category_controller:
        return g.category_controller.create_category()
    return jsonify({'error': 'Controller not found'}), 500


@category_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete(id: int):
    if g.category_controller:
        return g.category_controller.delete_category(id)
    return jsonify({'error': 'Controller not found'}), 500


@category_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    if g.category_controller:
        return g.category_controller.update_category(id)
    return jsonify({'error': 'Controller not found'}), 500


@category_bp.route('/list', methods=['GET'])
def list_categories():
    if g.category_controller:
        return g.category_controller.list_category()
    return jsonify({'error': 'Controller not found'}), 500


@category_bp.route('/list/<int:id>', methods=['GET'])
def list_category_by_id(id: int):
    if g.category_controller:
        return g.category_controller.list_category_by_id(id)
    return jsonify({'error': 'Controller not found'}), 500
