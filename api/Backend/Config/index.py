from datetime import datetime, timedelta
import os
from flask import jsonify
import jwt
from dotenv import load_dotenv as dotenv

dotenv()


class Config:
    def __init__(self):
        self.db_host = os.getenv('DB_HOST') or 'localhost'
        self.db_name = os.getenv('DB_NAME') or 'saley_stock'
        self.db_user = os.getenv('DB_USER') or 'root'
        self.db_pass = os.getenv('DB_PASS') or ''
        self.db_port = os.getenv('DB_PORT') or 3306
        self.jwt_secret = os.urandom(64)
        self.jwt_hash = os.getenv('JWT_HASH') or 'HS512'
        self.redis_host = os.getenv('REDIS_HOST') or 'localhost'
        self.redis_port = os.getenv('REDIS_PORT') or 6379

    def jwt_token(self, user):
        expiration_delta = timedelta(hours=1)
        payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + expiration_delta
        }
        token = jwt.encode(payload, self.jwt_secret, algorithm=self.jwt_hash)
        return token

    def jwt_decode(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Missing authorization header'}), 401

        try:
            access_token = auth_header.split(' ')[1]
            payload = jwt.decode(access_token, secret_key=self.jwt_secret, algorithms=[self.jwt_hash])
            user_id = payload['user_id']
            return None
        except jwt.exceptions.InvalidTokenError:
            return jsonify({'error': 'Invalid or expired token'}), 401
