from pony.orm import *
from ..Config.index import Config
import time
from datetime import datetime

db = Database()
config = Config()

MAX_RETRIES = 5
RETRY_DELAY = 3  # Seconds


def connect_to_db():
    for i in range(MAX_RETRIES):
        try:
            db.bind(provider='mysql', host=config.db_host, user=config.db_user, passwd=config.db_pass,
                    db='saley_stock')
            print("Database connection successful!")
            return
        except OperationalError as e:
            print(f" {e}, retrying in {RETRY_DELAY} seconds ({i + 1}/{MAX_RETRIES})")
            time.sleep(RETRY_DELAY)


connect_to_db()


# Define the User model

class Category(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    products = Set('Product')
    suppliers = Set('CategorySupplier')
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class Unit(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    products = Set('Product')
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class Supplier(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    location = Optional(str)
    phone = Optional(str, max_len=20)
    email = Optional(str)
    inbound_stocks = Set('InboundStock')
    products = Set('ProductSupplier')
    categories = Set('CategorySupplier')
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class Client(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    contact = Optional(str)
    email = Optional(str)
    outbound_stocks = Set('OutboundStock')
    orders = Set('Order')
    product_client = Set('ProductClient')
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class Service(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    users = Set('User')
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str)
    password = Required(bytes)
    role = Required(str, sql_type='ENUM("Admin", "Magasinier", "Client", "Supplier")')
    name = Optional(str)
    cin = Optional(str, max_len=20)
    email = Optional(str)
    phone = Optional(str, max_len=20)
    service = Optional(Service)
    inbound_stocks = Set('InboundStock')
    outbound_stocks = Set('OutboundStock')
    inventory_audits = Set('InventoryAudit')
    deliveries = Set('Delivery')
    returns = Set('Return')
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class Product(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    image_name = Optional(str)
    category = Required(Category)
    unit = Required(Unit)
    expiration_date = Optional(str)
    unit_price = Optional(float)
    stock = Set('Stock')
    inbound_stocks = Set('InboundStock')
    outbound_stocks = Set('OutboundStock')
    clients = Set('ProductClient')
    suppliers = Set('ProductSupplier')
    inventory_audits = Set('InventoryAudit')
    order_items = Set('OrderItem')
    returns = Set('Return')
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class Stock(db.Entity):
    id = PrimaryKey(int, auto=True)
    product = Required(Product)
    stock_security = Optional(int)
    stock_max = Optional(int)
    exp_date = Optional(str)
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class InboundStock(db.Entity):
    id = PrimaryKey(int, auto=True)
    quantity = Required(int)
    product = Required(Product)
    date_in = Optional(str)
    supplier = Required(Supplier)
    unit_price = Optional(float)
    user = Required(User)
    tva_rate = Optional(float)
    exp_date = Optional(str)
    invoice = Optional(str)
    create_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.create_date = datetime.utcnow()


class OutboundStock(db.Entity):
    id = PrimaryKey(int, auto=True)
    quantity = Required(int)
    product = Required(Product)
    date_out = Optional(str)
    user = Required(User)
    client = Required(Client)
    create_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.create_date = datetime.utcnow()


class ProductClient(db.Entity):
    client = Required(Client)
    product = Required(Product)
    PrimaryKey(client, product)
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class ProductSupplier(db.Entity):
    supplier = Required(Supplier)
    product = Required(Product)
    PrimaryKey(supplier, product)
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class CategorySupplier(db.Entity):
    category = Required(Category)
    supplier = Required(Supplier)
    PrimaryKey(category, supplier)
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class InventoryAudit(db.Entity):
    id = PrimaryKey(int, auto=True)
    product = Required(Product)
    user = Required(User)
    audit_date = Optional(str)
    audit_quantity = Optional(int)
    audit_id_uniq = Optional(int)
    notes = Optional(str)
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class Order(db.Entity):
    id = PrimaryKey(int, auto=True)
    order_date = Optional(str)
    client = Required(Client)
    total_amount = Optional(float)
    status = Required(str, sql_type='ENUM("Pending", "Completed", "Cancelled")')
    order_items = Set('OrderItem')
    deliveries = Set('Delivery')
    returns = Set('Return')
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class OrderItem(db.Entity):
    order = Required(Order)
    product = Required(Product)
    quantity = Required(int)
    unit_price = Optional(float)
    PrimaryKey(order, product)
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class Delivery(db.Entity):
    id = PrimaryKey(int, auto=True)
    order = Required(Order)
    delivery_date = Optional(str)
    delivered_by = Required(User)
    status = Required(str, sql_type='ENUM("Pending", "Delivered", "Cancelled")')
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


class Return(db.Entity):
    id = PrimaryKey(int, auto=True)
    order = Required(Order)
    return_date = Optional(str)
    product = Required(Product)
    quantity = Required(int)
    reason = Optional(str)
    handled_by = Required(User)
    created_date = Optional(datetime, default=lambda: datetime.utcnow())
    updated_date = Optional(datetime, default=lambda: datetime.utcnow())

    def before_insert(self):
        self.created_date = datetime.utcnow()
        self.updated_date = datetime.utcnow()

    def before_update(self):
        self.updated_date = datetime.utcnow()


db.generate_mapping(create_tables=True)
