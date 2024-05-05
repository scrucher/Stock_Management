from datetime import datetime, timedelta
from os import getenv as env
from dotenv import load_dotenv
from flask import jsonify
import jwt


load_dotenv()

class Config:
    db_host = env('DB_HOST')
    db_name = env('DB_NAME')
    db_user = env('DB_USRNM')
    db_pass = env('DB_PASS')
    db_port = env('DB_PORT')
    jwt_secret = env('JWT_SECRET')
    jwt_hash = env('JWT_HASH')

    def jwt_token(user):
        """Generates a JWT access token containing the user's ID."""
        expiration_delta = timedelta(hours=1)
        payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + expiration_delta
        }
        token = jwt.encode(payload, Config.jwt_secret, algorithm=Config.jwt_hash)
        return token.decode('utf-8')

    def jwt_decode(request):
        """Requires valid JWT in the 'Authorization' header."""
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Missing authorization header'}), 401

        try:
            access_token = auth_header.split(' ')[1]
            payload = jwt.decode(access_token, secret_key=Config.jwt_secret, algorithms=[Config.jwt_hash])
            user_id = payload['user_id']
            # ... Load user from the database if needed ...
            return None
        except jwt.exceptions.InvalidTokenError:
            return jsonify({'error': 'Invalid or expired token'}), 401