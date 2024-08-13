import os
import unittest
from flask import current_app
from app import create_app
from app.mapping.response_schema import ResponseSchema
from app.services.response_message import ResponseBuilder

class HomeResourceTestCase(unittest.TestCase):

    def setUp(self):
        # Configura el entorno de pruebas
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Limpia el contexto de la aplicación después de cada prueba
        self.app_context.pop()
    
    def test_index(self):
        # Crea el mensaje esperado
        message = ResponseBuilder().add_message("Bienvenidos").add_status_code(200).add_data({'title': 'API Auth'}).build()

        # Crea un cliente para enviar solicitudes a la aplicación
        client = self.app.test_client(use_cookies=True)
        responseSchema = ResponseSchema()

        # Usa una variable de entorno para la URL base
        api_base_url = os.environ.get('API_BASE_URL', 'http://localhost:5000')
        
        # Envía una solicitud GET a la ruta de la API
        response = client.get(f'{api_base_url}/api/v1/')

        # Verifica que el estado de la respuesta sea 200
        self.assertEqual(response.status_code, 200)

        # Carga la respuesta JSON usando el esquema de respuesta
        response_data = responseSchema.load(response.get_json())

        # Verifica que los datos de la respuesta coincidan con el mensaje esperado
        self.assertEqual(message.message, response_data['message'])
        self.assertEqual(message.status_code, response_data['status_code'])
        self.assertEqual(message.data, response_data['data'])

if __name__ == '__main__':
    unittest.main()
