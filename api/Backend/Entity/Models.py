from pony.orm import *
from ..Config.index import Config
import time

db = Database()

MAX_RETRIES = 5
RETRY_DELAY = 3  # Seconds


def connect_to_db():
    for i in range(MAX_RETRIES):
        try:
            db.bind(provider='mysql', host=Config.db_host, user=Config.db_user, passwd=Config.db_pass,
                    db=Config.db_name)
            print("Database connection successful!")
            return
        except OperationalError as e:
            print(f" {e}, retrying in {RETRY_DELAY} seconds ({i + 1}/{MAX_RETRIES})")
            time.sleep(RETRY_DELAY)


connect_to_db()


# Define the User model


class UserModel(db.Entity):
    name = Required(str)
    email = Required(str)
    role = Required(str)
    restaurant_id = Required(int)
    password = Required(bytes)


# class Category(db.Entity):
class Region(db.Entity):
    name = Required(str)
    city = Set('City', reverse="region")
    restaurant = Set('Restaurant', reverse="region")


class City(db.Entity):
    name = Required(str)
    region = Required(Region)
    restaurant = Set('Restaurant', reverse="city")


class Restaurant(db.Entity):
    name = Required(str)
    city = Required(City)
    region = Required(Region)


class Supplier(db.Entity):
    name = Required(str)
    product = Set('Product', reverse="supplier")

class Category(db.Entity):
    name = Required(str)
    product = Set('Product', reverse="category")


class Unit(db.Entity):
    name = Required(str)
    product = Set('Product', reverse="unit")


class Product(db.Entity):
    name = Required(str)
    category = Required(Category)
    supplier = Required(Supplier)
    unit = Required(Unit)
    quantity = Required(int)
    price = Required(float)


class Stock(db.Entity):
    name = Required(str)


db.generate_mapping(create_tables=True)
