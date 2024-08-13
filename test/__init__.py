import pytest
from app import app as flask_app, db
import os

@pytest.fixture(scope='module')
def app():
    # Configurar la aplicación para pruebas
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_TEST_URL', 'postgresql://user:password@localhost/test_db')  # Cambia esto según tu configuración
    yield flask_app

@pytest.fixture(scope='module')
def client(app):
    # Proporcionar un cliente de pruebas
    return app.test_client()

@pytest.fixture(autouse=True)
def setup_db(app):
    # Configurar la base de datos antes de las pruebas
    with app.app_context():
        db.create_all()  # Crear todas las tablas
        yield
        db.drop_all()  # Eliminar todas las tablas después de las pruebas
