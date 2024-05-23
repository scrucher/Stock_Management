from flask import Flask, render_template
from pony.flask import Pony
from .User.userController import UserController
from .Entity.Models import connect_to_db

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='dev',
))


@app.route('/user/sign_up', methods=['POST'])
def sign_up():
    return UserController.create_user()


@app.route('/user/login', methods=['POST'])
def login():
    return UserController.login_user()


@app.route('/user/update', methods=['PATCH'])
def update_user():
    return UserController.update_user()


@app.route('/user/delete', methods=['DELETE'])
def delete_user():
    return UserController.delete_user()


Pony(app)
