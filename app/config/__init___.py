"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Crear instancia de la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)  # Cargar configuración desde Config

# Inicializar la base de datos
db = SQLAlchemy(app)

# Importar modelos
from app.models import User, Recipe, Ingredient, Diet, UserFavoriteRecipe, UserDiet, RecipeIngredient, RecipeDiet

# Importar rutas (si tienes)
# from app.routes import main as main_routes
# app.register_blueprint(main_routes)
"""
