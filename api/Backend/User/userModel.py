from pony.orm import *
from ..Config.index import Config

db = Database()
# Define the User model
class UserModel(db.Entity):
    name = Required(str)
    email = Required(str)
    password = Required(bytes)
db.bind(provider='mysql', host=Config.db_host, user='root', passwd=Config.db_pass, db=Config.db_name)
db.generate_mapping(create_tables=True)