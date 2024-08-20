from flask import *
from ..Utilities.DTO import JSONResponse


class ErrorHandling:

    @staticmethod
    def internal_server_error() -> JSONResponse:
        return jsonify({'error': 'Internal Server Error'}), 500

    @staticmethod
    def not_found(err) -> JSONResponse:
        return jsonify({'error': f"{err} Not Found Make Sure that you have"}), 404

    @staticmethod
    def bad_request() -> JSONResponse:
        return jsonify({'error': "Bad Request Please try Again in a while, if the error persist contact the support"}), 400

    @staticmethod
    def unauthorized() -> JSONResponse:
        return jsonify({'error': 'Unauthorized Access'}), 401

    @staticmethod
    def forbidden() -> JSONResponse:
        return jsonify({'error': 'Forbidden'}), 403

    @staticmethod
    def request_timeout(err) -> JSONResponse:
        return jsonify({'error': f"{err} Request Timeout"}), 408

    @staticmethod
    def service_unavailable() -> JSONResponse:
        return jsonify({'error': "Service Unavailable"}), 503

    @staticmethod
    def success_ok(data) -> JSONResponse:
        return jsonify({'data': data}), 200

    @staticmethod
    def success_created(msg) -> JSONResponse:
        return jsonify({'data': f'{msg} Created'}), 201
