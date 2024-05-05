from flask import request, jsonify
from .userModel import UserModel
from pony.orm import *
from pony.orm import db_session, commit


class UserController:
    def __init__(self):
        self.user_modal = UserModel()

    @db_session
    def create_user():
        data = request.get_json()
        try:
            result = UserModel.get(email=data["email"])
            if result:
                return jsonify({'message': 'User Not Found '})
            else:
                UserModel(
                    name=data["name"],
                    email=data["email"],
                    password=data["password"]
                )
                commit()  # Save the changes to the database
                return jsonify({'message': 'User created successfully'})
        except Exception as e:
            return jsonify({'error': str(e)})






