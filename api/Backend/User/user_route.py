from flask import Blueprint
from .userController import UserController

user_bp = Blueprint('user_bp', __name__)
user_controller = UserController()


@user_bp.route('/sign_up', methods=['POST'])
def create_user():
    return user_controller.create_user()


@user_bp.route('/get_user/<int:id>', methods=['GET'])
def get_user(user_id):
    return user_controller.get_user(user_id)


@user_bp.route('/users', methods=['GET'])
def get_users():
    return user_controller.get_all_users()


@user_bp.route('/user_update/<int:id>', methods=['PUT'])
def update_user(id):
    return user_controller.update_user(id)


@user_bp.route('/user_delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    return user_controller.delete_user_by_id(id)


@user_bp.route('/login', methods=['POST'])
def login():
    return user_controller.login_user()

