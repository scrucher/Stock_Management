from pony.orm import *
from ..Config.index import db_connection

db = Database()
# Define the User model
class UserModel(db.Entity):
    name = Required(str)
    email = Required(str)
    password = Required(str)
db.bind(provider='mysql', host='localhost', user='root', passwd='', db='saley_stock')
db.generate_mapping(create_tables=True)