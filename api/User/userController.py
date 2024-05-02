import sys
sys.path.append('../')
from Config import index

class UserController:
    def __init__(self):
        self.db = index.db
        self.db.connect()

    def Login(name, email, password, role):
        return 1



