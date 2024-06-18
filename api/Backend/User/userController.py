from flask import request, jsonify
from ..Entity.Models import User
from ..Config.index import Config
from pony.orm import *
import bcrypt


class UserController:

    @db_session
    def create_user(self):
        data = request.get_json()
        try:
            result = User.get(email=data["email"])
            if result:
                return jsonify({'message': 'User Not Found '}), 404
            else:
                salt = bcrypt.gensalt()
                password = bcrypt.hashpw(
                    data['password'].encode('utf-8'),
                    salt  # Generate a strong salt
                )
                User(
                    name=data['name'],
                    username=data['username'],
                    email=data["email"],
                    role=data["role"],
                    password=password,
                    phone=data["phone"],
                    cin=data["cin"],
                    service=data["service"]
                )
                commit()  # Save the changes to the database
                return jsonify({'message': 'User created successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def login_user(self):
        data = request.get_json()
        try:
            result = User.get(email=data["email"])
            if not result:
                return jsonify({'message': 'User Not Found'}), 404
            else:
                res = User.get(email=data["email"])
                if res and bcrypt.checkpw(
                        data['password'].encode('utf-8'),
                        res.password
                ):
                    token = Config.jwt_token(res)
                    response = jsonify({'message': 'Login successful'})
                    response.set_cookie(
                        'access_token', token, httponly=True, secure=True
                    )
                    return response
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update_user(self, id):
        data = request.get_json()
        try:
            user = User.get(id=data["id"])
            user.set(
                name=data.get('name', user.name),
                username=data.get('username', user.username),
                email=data.get('email', user.email),
                role=data.get('role', user.role),
                phone=data.get('phone', user.phone),
                cin=data.get('cin', user.cin),
                service=data.get('service', user.service)
            )
            commit()
            return jsonify({'message': 'User updated successfully'})
        except Exception as e:
            return jsonify({'error': str(e)})

    def delete_user(self):
        data = request.get_json()
        try:
            user = User.get(id=data["id"])
            if not user:
                return jsonify({'message': 'User Not Found'})
            User['id'].delete()
            commit()
            return jsonify({'message': 'User deleted successfully'})
        except Exception as e:
            return jsonify({'error': str(e)})

    def get_user(self, id):
        try:
            user = User.get(id=id)
            if not user:
                return jsonify({'message': 'User Not Found'}), 404
            return user
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_all_users(self):
        try:
            user = select(u for u in User)[:]
            if not user:
                return jsonify({'message': 'Users Not Found'}), 404
            return user
        except Exception as e:
            return jsonify({'error': str(e)}), 500


    def delete_all_users(self):
        try:
            user = select(u for u in User)[:]
            if not user:
                return jsonify({'message': 'Users Not Found'}), 404
            user.remove()
            return jsonify({'message': 'Users deleted successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete_user_by_id(self, id):
        try :
            user = User.get(id=id)
            if not user:
                return jsonify({'message': 'User Not Found'}), 404
            user.remove()
            return jsonify({'message': 'User deleted successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500