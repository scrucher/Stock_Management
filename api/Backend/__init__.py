from flask import Flask, render_template
from pony.flask import Pony
from .Config.index import db_connection
from .User.userController import UserController

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='dev',
    ))
@app.route('/sign_up', methods=['POST'])
def sign_up():
    return UserController.create_user()

Pony(app)