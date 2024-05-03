import sys
from flask import request

class UserController:
    def __init__(self):
        pass
    def login(self):
        data = request.json()
        print(data)



