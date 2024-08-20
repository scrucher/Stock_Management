from flask import Flask, g
from flask_cors import CORS
from .User.user_route import user_bp
from .Service.Service_Route import service_bp
from .Category.Category_Route import category_bp
from .Category.Category_Repository import CategoryRepository
from .Category.Category_Controller import CategoryController
from .Unit.Unit_route import unit_bp
from .Unit.Unit_controller import UnitController
from .Unit.Unit_Repository import UnitRepository
from .Product.Product_Route import product_bp
from .Product.Product_Repository import ProductRepository
from .Product.Product_Controller import ProductController
from .Supplier.Supplier_Route import supplier_bp
from .Supplier.Supplier_Repository import SupplierRepository
from .Supplier.Supplier_Controller import SupplierController
from .Utilities.Redis_Client import RedisClient
from .Utilities.PreloadData import PreloadData
from .Service.Service_Repository import ServiceRepository
from .Service.Service_Controller import ServiceController
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
        redis_client = RedisClient()
        category_repository = CategoryRepository()
        unit_repository = UnitRepository()
        service_repository = ServiceRepository()
        product_repository = ProductRepository()
        supplier_repository = SupplierRepository()
        preload_data = PreloadData(redis_client,
                                   category_repository,
                                   unit_repository,
                                   product_repository,
                                   )
        category_controller = CategoryController(category_repository, redis_client)
        unit_controller = UnitController(unit_repository, redis_client)
        service_controller = ServiceController(service_repository, redis_client)
        product_controller = ProductController(product_repository, redis_client)
        supplier_controller = SupplierController(supplier_repository, redis_client)

        @app.before_request
        def before_request():
            g.category_controller = category_controller
            g.unit_controller = unit_controller
            g.service_controller = service_controller
            g.product_controller = product_controller
            g.supplier_controller = supplier_controller

        CORS(app, resources={r"/*": {"origins": "*"}})
        app.config['CORS_HEADERS'] = 'Content-Type'
        app.register_blueprint(user_bp, url_prefix='/User')
        app.register_blueprint(service_bp, url_prefix='/Service')
        app.register_blueprint(category_bp, url_prefix='/Category')
        app.register_blueprint(unit_bp, url_prefix='/Unit')
        app.register_blueprint(product_bp, url_prefix='/Product')
        app.register_blueprint(supplier_bp, url_prefix='/Supplier')

    return app
