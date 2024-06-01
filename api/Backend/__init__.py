from flask import Flask
from pony.flask import Pony
from .Entity.Models import connect_to_db
from .User.user_route import user_bp
from .Service.Service_Route import service_bp
from .Category.Category_Route import category_bp
from .Unit.Unit_route import unit_bp
from .Product.Product_Route import product_bp
from .InStock.Instock_Route import in_stock_bp
from .Supplier.Supplier_Route import supplier_bp


app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='dev',
))

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(service_bp, url_prefix='/services')
app.register_blueprint(category_bp, url_prefix='/category')
app.register_blueprint(unit_bp, url_prefix='/unit')
app.register_blueprint(product_bp, url_prefix='/product')
app.register_blueprint(in_stock_bp, url_prefix='/in_stock')
app.register_blueprint(supplier_bp, url_prefix='/supplier')

Pony(app)
