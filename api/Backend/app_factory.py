from flask import Flask, g
from flask_cors import CORS
from .User.user_route import user_bp
from .Service.Service_Route import service_bp
from .Category.Category_Route import category_bp  # Make sure this import is correct
from .Category.Category_Controller import CategoryController  # Make sure this import is correct
from .Category.Category_Repository import CategoryRepository  # Make sure this import is correct
from .Unit.Unit_route import unit_bp
from .Product.Product_Route import product_bp
from .Supplier.Supplier_Route import supplier_bp
from .Utilities.Redis_Client import RedisClient
from .Utilities.SearchAlgorithms import SearchAlgorithms
import os
from pony.flask import Pony


def create_app():
    app = Flask(__name__)
    with app.app_context():
        Pony(app)
        app.config.update(dict(
            DEBUG=True,
            SECRET_KEY=os.urandom(24),
        ))

        # Initialize Redis client and Category repository
        redis_client = RedisClient()
        category_repository = CategoryRepository()
        search_algorithms = SearchAlgorithms()

        # Initialize the Category controller with dependencies
        category_controller = CategoryController(category_repository, search_algorithms,redis_client)

        @app.before_request
        def before_request():
            g.category_controller = category_controller

        CORS(app, resources={r"/*": {"origins": "*"}})
        app.config['CORS_HEADERS'] = 'Content-Type'

        # Register blueprints
        app.register_blueprint(user_bp, url_prefix='/User')
        app.register_blueprint(service_bp, url_prefix='/Service')
        app.register_blueprint(category_bp, url_prefix='/Category')
        app.register_blueprint(unit_bp, url_prefix='/Unit')
        app.register_blueprint(product_bp, url_prefix='/Product')
        app.register_blueprint(supplier_bp, url_prefix='/Supplier')

    return app
