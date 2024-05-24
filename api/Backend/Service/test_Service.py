import unittest
from unittest.mock import patch, MagicMock
from flask import jsonify, Flask
from pony.orm import *
from ..Entity.Models import Service, db
from .Service_Controller import ServiceController
from .Service_Route import service_bp



class TestServiceController(unittest.TestCase):

    def setUp(self):
        self.controller = ServiceController()

    @patch('Service_Controller.request')
    @patch('Service_Controller.Service')
    def test_create_service(self, mock_service, mock_request):
        mock_request.get_json.return_value = {'name': 'Test Service'}
        response = self.controller.create_service()
        self.assertEqual(response[1], 201)
        mock_service.assert_called_with(name='Test Service')

    @patch('Service_Controller.request')
    @patch('Service_Controller.Service')
    def test_delete_services(self, mock_service, mock_request):
        mock_request.get_json.return_value = {'id': 1}
        mock_service.get.return_value = MagicMock()
        response = self.controller.delete_services()
        self.assertEqual(response[1], 200)
        mock_service.get.return_value.delete.assert_called_once()

    @patch('Service_Controller.request')
    @patch('Service_Controller.Service')
    def test_update_service(self, mock_service, mock_request):
        mock_request.get_json.return_value = {'name': 'Updated Service'}
        mock_service.get.return_value = MagicMock()
        response = self.controller.update_service(1)
        self.assertEqual(response[1], 200)
        mock_service.get.return_value.set.assert_called_with(name='Updated Service')

    @patch('Service_Controller.Service')
    def test_list_services(self, mock_service):
        mock_service.select.return_value = [MagicMock(to_dict=lambda: {'name': 'Test Service'})]
        response = self.controller.list_services()
        self.assertEqual(response[1], 200)
        self.assertIn('services', response[0].json)

    @patch('Service_Controller.Service')
    def test_list_service_by_id(self, mock_service):
        mock_service.get.return_value = MagicMock(to_dict=lambda: {'name': 'Test Service'})
        response = self.controller.list_service_by_id(1)
        self.assertEqual(response[1], 200)
        self.assertIn('services', response[0].json)




class TestServiceRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(service_bp, url_prefix='/service')
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        db.bind(provider='sqlite', filename=':memory:')  # Use an in-memory database for testing
        db.generate_mapping(create_tables=True)

    def test_create_service(self):
        response = self.client.post('/service/create', json={'name': 'Test Service'})
        self.assertEqual(response.status_code, 201)

    def test_delete_services(self):
        # First, create a service to delete
        with db_session:
            service = Service(name='Test Service')
        response = self.client.delete('/service/delete', json={'id': service.id})
        self.assertEqual(response.status_code, 200)

    def test_update_service(self):
        # First, create a service to update
        with db_session:
            service = Service(name='Test Service')
        response = self.client.put(f'/service/update/{service.id}', json={'name': 'Updated Service'})
        self.assertEqual(response.status_code, 200)

    def test_list_services(self):
        response = self.client.get('/service/list')
        self.assertEqual(response.status_code, 200)

    def test_list_service_by_id(self):
        # First, create a service to retrieve
        with db_session:
            service = Service(name='Test Service')
        response = self.client.get(f'/service/list/{service.id}')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()