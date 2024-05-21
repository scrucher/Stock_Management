from datetime import datetime, timedelta
import os
from flask import jsonify
import jwt
from dotenv import load_dotenv as dotenv

dotenv()


class Config:
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_port = os.getenv('DB_PORT')
    jwt_secret = os.getenv('JWT_SECRET')
    jwt_hash = os.getenv('JWT_HASH')

    def jwt_token(user):
        expiration_delta = timedelta(hours=1)
        payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + expiration_delta
        }
        token = jwt.encode(payload, Config.jwt_secret, algorithm=Config.jwt_hash)
        return token

    def jwt_decode(request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Missing authorization header'}), 401

        try:
            access_token = auth_header.split(' ')[1]
            payload = jwt.decode(access_token, secret_key=Config.jwt_secret, algorithms=[Config.jwt_hash])
            user_id = payload['user_id']
            return None
        except jwt.exceptions.InvalidTokenError:
            return jsonify({'error': 'Invalid or expired token'}), 401
