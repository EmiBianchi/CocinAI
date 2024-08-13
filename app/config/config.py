# Importar el logger de asyncio para registrar eventos y errores
from asyncio.log import logger
# Cargar variables de entorno desde un archivo .env
from dotenv import load_dotenv
# Para gestionar rutas de archivos
from pathlib import Path
# Importar el módulo os para interactuar con el sistema operativo
import os

# Definir la ruta base del proyecto, que es dos niveles arriba de este archivo
basedir = os.path.abspath(Path(__file__).parents[2])
# Cargar las variables de entorno desde el archivo .env ubicado en la ruta base
load_dotenv(os.path.join(basedir, '.env'))

# Clase base de configuración
class Config(object):
    # Indica si la aplicación está en modo de pruebas
    TESTING = False
    # Deshabilita el seguimiento de modificaciones en las instancias de SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Habilita el registro de consultas SQL en el entorno de la aplicación
    SQLALCHEMY_RECORD_QUERIES = True
    
    # Método estático para inicializar la aplicación con esta configuración
    @staticmethod
    def init_app(app):
        pass  # Aquí se pueden agregar configuraciones específicas para la aplicación

# Clase de configuración para pruebas
class TestConfig(Config):
    # Indica que la aplicación está en modo de pruebas
    TESTING = True
    # Habilita el modo de depuración
    DEBUG = True
    # Habilita el seguimiento de modificaciones en las instancias de SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Establece la URI de la base de datos de pruebas desde las variables de entorno
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')

# Clase de configuración para desarrollo
class DevelopmentConfig(Config):
    # Indica que la aplicación está en modo de pruebas
    TESTING = True
    # Habilita el modo de depuración
    DEBUG = True
    # Habilita el seguimiento de modificaciones en las instancias de SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Establece la URI de la base de datos de desarrollo desde las variables de entorno
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

# Clase de configuración para producción
class ProductionConfig(Config):
    # Deshabilita el modo de depuración
    DEBUG = False
    # Indica que la aplicación no está en modo de pruebas
    TESTING = False
    # Deshabilita el registro de consultas SQL en el entorno de producción
    SQLALCHEMY_RECORD_QUERIES = False
    # Establece la URI de la base de datos de producción desde las variables de entorno
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URI')
    
    # Método de clase para inicializar la aplicación con esta configuración
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

# Función de fábrica para crear la configuración basada en el entorno
def factory(app):
    # Diccionario que asocia entornos con sus respectivas configuraciones
    configuration = {
        'testing': TestConfig,
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }
    
    # Devuelve la configuración correspondiente al entorno especificado en la aplicación
    return configuration[app]
