from flask import Flask, render_template
from pony.flask import Pony
from .User.userController import UserController
from .Entity.Models import connect_to_db
from .User.user_route import user_bp

usr_cntrl = UserController()
app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='dev',
))

app.register_blueprint(user_bp, url_prefix='/users')


Pony(app)
