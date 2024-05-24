from flask import Flask
from pony.flask import Pony
from .Entity.Models import connect_to_db
from .User.user_route import user_bp
from .Service.Service_Route import service_bp

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='dev',
))

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(service_bp, url_prefix='/services')

Pony(app)
