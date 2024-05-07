from flask import request, jsonify
from .userModel import UserModel
from ..Config.index import Config
from pony.orm import *
import bcrypt


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
                salt = bcrypt.gensalt()
                password =bcrypt.hashpw(
                            data['password'].encode('utf-8'),
                            salt # Generate a strong salt
                            )
                UserModel(
                    name=data["name"],
                    email=data["email"],
                    password=password
                )
                commit()  # Save the changes to the database
                return jsonify({'message': 'User created successfully'})
        except Exception as e:
            return jsonify({'error': str(e)})

    def login_user():
        data = request.get_json()
        try:
            result = UserModel.get(email=data["email"])
            if not result:
                return jsonify({'message': 'User Not Found'})
            else:
                res = UserModel.get(email=data["email"])
                if res and bcrypt.checkpw(
                        data['password'].encode('utf-8'),
                        res.password.encode('utf-8')
                ):
                    token = Config.jwt_token(res)
                    response = jsonify({'message': 'Login successful'})
                    response.set_cookie(
                        'access_token', token, httponly=True, secure=True
                    )
                    return response
        except Exception as e:
            return jsonify({'error': str(e)})







